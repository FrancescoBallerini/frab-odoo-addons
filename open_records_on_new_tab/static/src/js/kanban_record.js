odoo.define('open_records_on_new_tab.KanbanRecord', function (require) {
    "use strict";

    var KanbanRecord = require('web.KanbanRecord');

    KanbanRecord.include({
        events: _.extend({}, KanbanRecord.prototype.events, {
            'mousedown': '_onRecordMouseDown',
        }),

        /**
         * Helper method to open record in new tab
         */
        _openRecordNewTab: function () {
            if (this.$el.hasClass('o_currently_dragged')) {
                // this record is currently being dragged and dropped, so we do not
                // want to open it.
                return;
            }
            var editMode = this.$el.hasClass('oe_kanban_global_click_edit');
            this.trigger_up('open_record', {
                id: this.db_id,
                mode: editMode ? 'edit' : 'readonly',
                openInNewTab: true
            });
        },

        /**
         * Override _onGlobalClick to handle Ctrl+Click and Cmd+Click
         */
        _onGlobalClick: function (event) {
            if (event.ctrlKey || event.metaKey) {
                // Replicate all the checks from the parent method
                if ($(event.target).parents('.o_dropdown_kanban').length) {
                    return;
                }
                var trigger = true;
                var elem = event.target;
                var ischild = true;
                var children = [];
                while (elem) {
                    var events = $._data(elem, 'events');
                    if (elem === event.currentTarget) {
                        ischild = false;
                    }
                    var test_event = events && events.click && (events.click.length > 1 || events.click[0].namespace !== 'bs.tooltip');
                    var testLinkWithHref = elem.nodeName.toLowerCase() === 'a' && elem.href;
                    if (ischild) {
                        children.push(elem);
                        if (test_event || testLinkWithHref) {
                            // Do not trigger global click if one child has a click
                            // event registered (or it is a link with href)
                            trigger = false;
                        }
                    }
                    if (trigger && test_event) {
                        _.each(events.click, function (click_event) {
                            if (click_event.selector) {
                                // For each parent of original target, check if a
                                // delegated click is bound to any previously found children
                                _.each(children, function (child) {
                                    if ($(child).is(click_event.selector)) {
                                        trigger = false;
                                    }
                                });
                            }
                        });
                    }
                    elem = elem.parentElement;
                }

                if (trigger) {
                    // Open in new tab instead of normal open
                    this._openRecordNewTab();
                }
                return;
            }

            // Normal click - execute unpatched method
            return this._super.apply(this, arguments);
        },

        /**
         * Handle middle mouse button (mousewheel) click to open in new tab
         */
        _onRecordMouseDown: function (ev) {
            if (ev.button === 1 || ev.which === 2) {
                ev.preventDefault();
                ev.stopPropagation();

                // Replicate all the checks from _onGlobalClick
                if ($(ev.target).parents('.o_dropdown_kanban').length) {
                    return;
                }
                var trigger = true;
                var elem = ev.target;
                var ischild = true;
                var children = [];
                while (elem) {
                    var events = $._data(elem, 'events');
                    if (elem === ev.currentTarget) {
                        ischild = false;
                    }
                    var test_event = events && events.click && (events.click.length > 1 || events.click[0].namespace !== 'bs.tooltip');
                    var testLinkWithHref = elem.nodeName.toLowerCase() === 'a' && elem.href;
                    if (ischild) {
                        children.push(elem);
                        if (test_event || testLinkWithHref) {
                            trigger = false;
                        }
                    }
                    if (trigger && test_event) {
                        _.each(events.click, function (click_event) {
                            if (click_event.selector) {
                                _.each(children, function (child) {
                                    if ($(child).is(click_event.selector)) {
                                        trigger = false;
                                    }
                                });
                            }
                        });
                    }
                    elem = elem.parentElement;
                }

                if (trigger) {
                    this._openRecordNewTab();
                }
            }
        },
    });

    return KanbanRecord;
});
