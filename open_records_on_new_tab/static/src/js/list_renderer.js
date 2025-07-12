/** @odoo-module **/

import { ListRenderer } from "@web/views/list/list_renderer";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { containsActiveElement } from "@web/core/utils/ui";

const { onMounted, useRef } = owl;


patch(ListRenderer.prototype, 'open_records_on_new_tab.ListRenderer', {
    setup() {
        this._super(...arguments);
        this.router = useService("router");
        this.tableRef = useRef('table');

        onMounted(this.bindMouseDownHandler.bind(this));
    },

    bindMouseDownHandler() {
        // Bind mousedown event handler when component is mounted: this is needed
        // for the mouse wheel click since onCellClicked doesn't get triggered by it
        const table = this.tableRef.el;
        if (!table) return;

        const tbody = table.querySelector('tbody');
        if (!tbody) return;

        // Bind mousedown handler on every listview row
        const rows = tbody.querySelectorAll('tr[data-id]');
        rows.forEach(row => {
            row.addEventListener('mousedown', this.handleMouseDown.bind(this));
        });
    },

    handleMouseDown(ev) {
        if (ev.button === 1) { // Middle mouse button
            const row = ev.currentTarget;

            // Execute only essential checks for middle-click
            if (ev.target.special_click) {
                return;
            }

            if (this.props.archInfo.noOpen) {
                return;
            }

            if (this.isX2Many) {
                return;
            }

            // Get record by row index
            const rowIndex = Array.from(row.parentNode.children).indexOf(row);

            if (rowIndex >= 0 && rowIndex < this.props.list.records.length) {
                const record = this.props.list.records[rowIndex];
                this._openRecordInNewTab(record);
            }
        }
    },


    /**
     * Override onCellClicked to handle Ctrl+Click for opening in new tab
     */
    async onCellClicked(record, column, ev) {
        if (ev.ctrlKey || ev.metaKey) {
            // BUG FIX: Don't open in new tab if we're in a x2many ListView
            // This prevents opening wrong records (e.g., account.move with account.move.line ID)
            if (this.isX2Many) {
                // For x2many ListView, use normal behavior
                return this._super(record, column, ev);
            }

            // Execute all the same checks as the original method
            if (ev.target.special_click) {
                return;
            }
            const recordAfterResequence = async () => {
                const recordIndex = this.props.list.records.indexOf(record);
                await this.resequencePromise;
                // row might have changed record after resequence
                record = this.props.list.records[recordIndex] || record;
            };

            if ((this.props.list.model.multiEdit && record.selected) || this.isInlineEditable(record)) {
                if (record.isInEdition && this.props.list.editedRecord === record) {
                    const cell = this.tableRef.el.querySelector(
                        `.o_selected_row td[name='${column.name}']`
                    );
                    if (cell && containsActiveElement(cell)) {
                        this.lastEditedCell = { column, record };
                        // Cell is already focused.
                        return;
                    }
                    this.focusCell(column);
                    this.cellToFocus = null;
                } else {
                    await recordAfterResequence();
                    await record.switchMode("edit");
                    this.cellToFocus = { column, record };
                }
            } else if (this.props.list.editedRecord && this.props.list.editedRecord !== record) {
                this.props.list.unselectRecord(true);
            } else if (!this.props.archInfo.noOpen) {
                // open in new tab instead of calling this.props.openRecord(record)
                this._openRecordInNewTab(record);
            }
            return;
        }

        // Normal click (no Ctrl/Cmd) - execute default behavior
        return this._super(record, column, ev);
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
    }
});
