odoo.define('open_records_on_new_tab.AbstractController', function (require) {
    "use strict";

    var AbstractController = require('web.AbstractController');

    AbstractController.include({
        /**
         * Override _onOpenRecord to handle opening in new tab
         * @override
         */
        _onOpenRecord: function (ev) {
            if (ev.data.openInNewTab) {
                ev.stopPropagation();
                var record = this.model.get(ev.data.id, {raw: true});

                // Get current hash parameters
                var hash = $.bbq.getState(true);

                // Build the URL for the form view
                var params = {
                    id: record.res_id,
                    view_type: 'form',
                    model: this.modelName,
                };

                // Preserve action if available
                if (hash.action) {
                    params.action = hash.action;
                }

                // Preserve menu_id if available
                if (hash.menu_id) {
                    params.menu_id = hash.menu_id;
                }

                var url = window.location.origin + '/web#' + $.param(params);
                window.open(url, '_blank');
                return;
            }

            // Normal behavior - execute unpatched handler
            return this._super.apply(this, arguments);
        },
    });

    return AbstractController;
});
