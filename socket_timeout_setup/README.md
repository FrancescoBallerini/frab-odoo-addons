Module Description
---------------
- Give control on socket timeout from options configuration file and UI Settings/Technical/System Parameters menu
- Only for multi-thread configuration (workers enabled)

More info about socket timeout:

The ODOO_HTTP_SOCKET_TIMEOUT environment variable allows to control socket timeout for
extreme latency situations. It's generally better to use a good buffering reverse proxy
to quickly free workers rather than increasing this timeout to accommodate high network
latencies & b/w saturation. This timeout is also essential to protect against accidental
DoS due to idle HTTP connections.

Socket timeout is generally setup by ODOO_HTTP_SOCKET_TIMEOUT environment variable, otherwise it will have a
default value of 2 seconds. This module allows to set socket timeout for multi-thread configuration
in 2 additional ways.

Usage
---------------

- set a variable named 'socket_timeout' in your configuration and give and give an integer value (seconds)
  

- set a value for generated key 'socket_timeout_setup.timeout_value' in Settings/Technical/System Parameters menu.
  It will change the socket timeout value at runtime.

How timeout is evaluated:

If both value are set, the System Parameter have priority. <br/>
If both value are not set or invalid (not integer values), the default workflow will be restored so the
value will be taken from 'ODOO_HTTP_SOCKET_TIMEOUT' environment variable, if set, or it will be the default hardcoded value (2 seconds).

To disable 'socket_timeout_setup.timeout_value', set it to 0.

Warning
---------------
Used/tested on odoo14 packaged installation on:

<h4>Version</h4>

Odoo 14.0 Community Edition 

Installed with https://www.odoo.com/documentation/14.0/administration/install/install.html#packaged-installers

<h4>Server</h4>

ubuntu 20.04 <br/>
16GB of RAM <br/>
16 CPUs <br/>
No reverse proxy (no NGINX) <br/>


<h4>Other configuration params</h4>

workers = 30<br/>
limit_memory_hard = 2684354560 <br/>
limit_memory_soft = 2147483648 <br/>
limit_request = 8192<br/>
limit_time_cpu = 600<br/>
limit_time_real = 1200<br/>
limit_time_real_cron = -1 <br/>
max_cron_threads = 2 <br/>
