odoo.define('open_records_on_new_tab.ListRenderer', function (require) {
    "use strict";

    var ListRenderer = require('web.ListRenderer');

    ListRenderer.include({
        events: _.extend({}, ListRenderer.prototype.events, {
            'mousedown tbody tr': '_onRowMouseDown',
        }),

        /**
         * Override _onRowClicked: if Ctrl key is pressed simultaneously with click
         * open the record in a new tab
         */
        _onRowClicked: function (ev) {
            if (ev.ctrlKey || ev.metaKey) {
                // We need to manually call open_record with a new openInNewTab argument,
                // because it's not possible to access the 'click' event (and therefore the key pressed)
                // once the open_record event is triggered
                if (!ev.target.closest('.o_list_record_selector') && !$(ev.target).prop('special_click')) {
                    var id = $(ev.currentTarget).data('id');
                    if (id) {
                        this.trigger_up('open_record', {
                            id: id,
                            target: ev.target,
                            openInNewTab: true
                        });
                        return;
                    }
                }
            } else {
                // Normal click - execute unpatched code
                return this._super.apply(this, arguments);
            }
        },

        /**
         * If the record is clicked using the 'mousewheel' open the record in a new tab.
         * Note: an additional handler for mousewheel is necessary because the click of
         * this button doesn't trigger the 'click' event but the 'mousedown' event
         */
        _onRowMouseDown: function (ev) {
            if (ev.button === 1 || ev.which === 2) {
                ev.preventDefault();
                ev.stopPropagation();

                if (!ev.target.closest('.o_list_record_selector') && !$(ev.target).prop('special_click')) {
                    var id = $(ev.currentTarget).data('id');
                    if (id) {
                        this.trigger_up('open_record', {
                            id: id,
                            target: ev.target,
                            openInNewTab: true
                        });
                    }
                }
            }
        },

    });

    return ListRenderer;
});
