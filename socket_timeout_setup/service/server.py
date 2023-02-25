import logging
import errno
import fcntl
import socket
import threading

import odoo
import odoo.service.server as srv
from odoo import api, SUPERUSER_ID
from odoo.tools import config as configfile

_logger = logging.getLogger(__name__)


def fetch_timeout_val_from_params(db_name, timeout_values):
    with odoo.api.Environment.manage():
        with odoo.registry(db_name).cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            sys_param_timeout = env['ir.config_parameter'].sudo().get_param(
                'socket_timeout_setup.timeout_value'
            )
            err = False
            if sys_param_timeout:
                try:
                    sys_param_timeout = int(sys_param_timeout)
                except:
                    err = 'Wrong value for system parameter \'sys_param_timeout\' ' \
                          '(%s). Parameter value must be integer. Set to 0 to disable ' \
                          'parameter, default value will be taken.' % sys_param_timeout
                    _logger.warning(err)
                if not err:
                    timeout_values.update({
                        'sys_param_timeout': sys_param_timeout
                    })
            return timeout_values


class WorkerHttpProcessRequestPatch(srv.WorkerHTTP):

    def process_request(self, client, addr):

        """ @override: check for socket_timeout in odoo.conf, if not found
        check for value in ir.config.parameter (possible to change value
        at runtime without restarting the server). If not found, use the
        value stored in init (environment variable if found, or default) """

        timeout_values = dict()
        config_socket_timeout = configfile.get('socket_timeout')
        err = False

        if config_socket_timeout:
            try:
                config_socket_timeout = int(config_socket_timeout)
            except:
                err = 'Wrong value for odoo configuration file in \'socket_timeout\' ' \
                      'variable: %s. Value must be integer.' % config_socket_timeout
                _logger.warning(err)

            if not err:
                timeout_values.update({
                    'config_socket_timeout': config_socket_timeout
                })

        # this is the only way i found to get dbname in case user
        # takes his choice by settings menu:
        # - request.env.session.db returns 'unbound obj'
        # - odoo.tools.config['db_name'] might be False
        # Found a couple of use case in _get_db() method of
        # GettextAlias class and odoo/tools/mail
        db_name = getattr(threading.currentThread(), 'dbname', None)

        if db_name:
            fetch_timeout_val_from_params(db_name, timeout_values)

        timeout_config_or_sysparam = None
        if timeout_values:
            if 'config_socket_timeout' in timeout_values and 'sys_param_timeout' in timeout_values:
                # both values setup, take system parameter over odoo conf
                # since it can be updated without server restart
                if timeout_values['sys_param_timeout']:
                    timeout_config_or_sysparam = timeout_values['sys_param_timeout']
                else:
                    timeout_config_or_sysparam = timeout_values['config_socket_timeout']
            elif 'config_socket_timeout' in timeout_values and 'sys_param_timeout' not in timeout_values:
                timeout_config_or_sysparam = timeout_values['config_socket_timeout']
            elif 'config_socket_timeout' not in timeout_values and 'sys_param_timeout' in timeout_values:
                timeout_config_or_sysparam = timeout_values['sys_param_timeout']

        if timeout_config_or_sysparam:
            self.sock_timeout = timeout_config_or_sysparam

        client.setblocking(1)
        client.settimeout(self.sock_timeout)
        client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # Prevent fd inherientence close_on_exec
        flags = fcntl.fcntl(client, fcntl.F_GETFD) | fcntl.FD_CLOEXEC
        fcntl.fcntl(client, fcntl.F_SETFD, flags)
        # do request using BaseWSGIServerNoBind monkey patched with socket
        self.server.socket = client
        # tolerate broken pipe when the http client closes the socket before
        # receiving the full reply
        try:
            self.server.process_request(client, addr)
        except IOError as e:
            if e.errno != errno.EPIPE:
                raise
        self.request_count += 1


odoo.service.server.WorkerHTTP.process_request = WorkerHttpProcessRequestPatch.process_request
