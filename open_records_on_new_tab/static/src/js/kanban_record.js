/** @odoo-module **/

import { CANCEL_GLOBAL_CLICK, KanbanRecord } from "@web/views/kanban/kanban_record";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

const { onMounted, useRef } = owl;


patch(KanbanRecord.prototype, 'open_records_on_new_tab.KanbanRecord', {
    setup() {
        this._super(...arguments);
        this.router = useService("router");
        this.action = useService("action");
        this.rootRef = useRef('root');

        onMounted(this.bindMouseDownHandler.bind(this));
    },

    bindMouseDownHandler() {
        // Bind mousedown event handler when component is mounted: this is needed
        // for the mouse wheel click since onCellClicked doesn't get triggered by it
        const root = this.rootRef.el;
        if (!root) return;
        root.addEventListener('mousedown', this.handleMouseDown.bind(this));
    },

    handleMouseDown(ev) {
        if (ev.button === 1) { // Middle mouse button
            ev.preventDefault();
            ev.stopPropagation();

            const { archInfo, forceGlobalClick } = this.props;
            const record = this.props.record;

            // Check if we might be in a x2many context
            if (archInfo && (archInfo.field || archInfo.fieldName)) {
                return;
            }

            if (ev.target.closest(CANCEL_GLOBAL_CLICK)) {
                return;
            }

            if (!forceGlobalClick && archInfo.openAction) {
                this.action.doActionButton({
                    name: archInfo.openAction.action,
                    type: archInfo.openAction.type,
                    resModel: record.resModel,
                    resId: record.resId,
                    resIds: record.resIds,
                    context: record.context,
                    onClose: async () => {
                        await record.model.root.load();
                        record.model.notify();
                    },
                });
            } else if (forceGlobalClick || this.allowGlobalClick) {
                this._openRecordInNewTab(record);
            }
        }
    },

    /**
     * Override onGlobalClick to handle Ctrl+Click for opening in new tab
     */
    onGlobalClick(ev) {
        if (ev.ctrlKey || ev.metaKey) {
            const { archInfo, forceGlobalClick } = this.props;
            const record = this.props.record;

            // BUG FIX: Check if we might be in a x2many context
            // If this kanban is part of a x2many field, use normal behavior for safety
            if (archInfo && (archInfo.field || archInfo.fieldName)) {
                // This suggests we're in a field context (likely x2many)
                return this._super(ev);
            }

            // Execute all the same checks as the original method
            if (ev.target.closest(CANCEL_GLOBAL_CLICK)) {
                return;
            }

            if (!forceGlobalClick && archInfo.openAction) {
                // For openAction, we still need to respect the original behavior
                // but we could potentially open in new tab - however this might break the action flow
                // Let's keep the original behavior for openAction to be safe
                this.action.doActionButton({
                    name: archInfo.openAction.action,
                    type: archInfo.openAction.type,
                    resModel: record.resModel,
                    resId: record.resId,
                    resIds: record.resIds,
                    context: record.context,
                    onClose: async () => {
                        await record.model.root.load();
                        record.model.notify();
                    },
                });
            } else if (forceGlobalClick || this.allowGlobalClick) {
                // open in new tab instead of calling openRecord(record)
                this._openRecordInNewTab(record);
            }
            return;
        }

        // Normal click - execute default behavior
        return this._super(ev);
    },


    /**
     * Open record in new browser tab
     */
    _openRecordInNewTab(record) {
        // Get current URL state to preserve context
        const currentState = this.router.current.hash;

        // Build URL for form view
        const params = {
            id: record.resId,
            view_type: 'form',
            model: record.resModel,
        };

        // Preserve action and menu_id if available
        if (currentState.action) {
            params.action = currentState.action;
        }
        if (currentState.menu_id) {
            params.menu_id = currentState.menu_id;
        }

        const url = window.location.origin + '/web#' + new URLSearchParams(params).toString();
        window.open(url, '_blank');
    },
});
