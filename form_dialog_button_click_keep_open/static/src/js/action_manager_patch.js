odoo.define("form_dialog_button_click_keep_open.action_manager_patch", function (
    require
) {
    "use strict";

    var ActionManager = require("web.ActionManager");

    var core = require("web.core");
    var _t = core._t;

    ActionManager.include({
        init: function (parent, userContext) {
            this.keep_dialog_active = {}; // see _onExecuteAction
            this._super.apply(this, arguments);
        },

        _onExecuteAction: function (ev) {
            if (
                _.has(ev.data, "action_data") &&
                _.has(ev.data.action_data, "keep_dialog_active")
            ) {
                // We initially bind current record info in ev.data.attrs because it
                // is the only way to propagate them from the FormController up to the
                // Action Manager. Unfortunately, we cannot anymore use local parameters,
                // so we have to map it on instance. I have tried both mapping on ev.data
                // .env.context and ev.data.action_data.context, I am not sure why, but I
                // think it is not consistent for some reason because don't find them in
                // subsequent methods. This will at least ensure readability of params
                // in method _handleAction/_executeCloseAction...
                this.keep_dialog_active = ev.data.action_data.keep_dialog_active;
            }
            this._super.apply(this, arguments);
        },

        _handleAction: function (action, options) {
            // o_btn_keep_open: the complete process (_closeDialog then do action) leads to a
            // small but annoying 'flicker' effect due to the dialog closing and re-opening.
            // This implementaton hijack the flow to the act window and skip close action.
            // Apparently less safe than o_btn_reopen, but shouldn't cause problems since
            // concurrent actions will be dropped by DropPrevious mixins.
            if (
                !_.isEmpty(this.keep_dialog_active) &&
                this.keep_dialog_active.additionalData.selector_mode ===
                    "o_btn_keep_open"
            ) {
                var act = Object.assign({}, this.keep_dialog_active);
                var viewID = act.additionalData.viewID;
                this.keep_dialog_active = {}; //empty prop to prevent loop

                return this.do_action({
                    type: "ir.actions.act_window",
                    name: act.additionalData.title,
                    res_model: act.record.model,
                    view_type: "form",
                    view_mode: "form",
                    view_id: viewID,
                    views: [[viewID, "form"]],
                    domain: act.record.domain,
                    res_id: act.record.res_id,
                    target: "new",
                    context: act.record.context,
                });
            } else {
                return this._super.apply(this, arguments);
            }
        },

        _executeCloseAction: function (action, options) {
            // o_btn_reopen: execute the whole process (close dialog) then re-open it
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                if (
                    !_.isEmpty(self.keep_dialog_active) &&
                    self.keep_dialog_active.additionalData.selector_mode ===
                        "o_btn_reopen"
                ) {
                    var act = Object.assign({}, self.keep_dialog_active);
                    var viewID = act.additionalData.viewID;
                    self.keep_dialog_active = {}; //empty prop to prevent loop

                    return self.do_action({
                        type: "ir.actions.act_window",
                        name: act.additionalData.title,
                        res_model: act.record.model,
                        view_type: "form",
                        view_mode: "form",
                        view_id: viewID,
                        views: [[viewID, "form"]],
                        domain: act.record.domain,
                        res_id: act.record.res_id,
                        target: "new",
                        context: act.record.context,
                    });
                }
            });
        },
    });
});
