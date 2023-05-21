odoo.define('form_dialog_button_click_keep_open.form_controller_patch', function (require) {
"use strict";

var FormController = require('web.FormController');

var core = require('web.core');
var _t = core._t;

FormController.include({

    /*
     * When a button is clicked on a Web Client Formview, regardless how
     * the event is managed, the event itself and some datas (e.g. button
     * attributes) will be propagated to the following private JS methods:
     *
     * _onButtonClicked > _callButtonAction > _executeButtonAction
     *
     * the last method _executeButtonAction will eventually trigger the Action
     * Manager event "execute_action" and will pass all necessary datas to it.
     *
     * So from this point the event will be delegated from FormController to the
     * Action Manager handling.
     *
     * What this patch does:
     * Basically if the class is found on the button bound to the event we will
     * make a backup of the action and ensure the propagation of the action
     * backup down to the action handler, so when action close will be called,
     * we wait for the promise to be resolved then re-open the dialog.
     *
     *
     * act manager handling stack
     *    _onExecuteAction > doAction > _handleAction > _executeCloseAction
     *    > _closeDialog > _onShowEffect (optional) > promise resolved
     *
     *   here we simply make another do_action and use the backup data to
     *   re-open the wizard, we have to make some re-bind to make sure that
     *   we bring all necessary data to _executeCloseAction method.
     *
     */

    _onButtonClicked: function (ev) {

        // If we read 'o_btn_keep_open' from button attributes we make a
        // backup of ev.data.attrs: basically we need to save current record
        // data since they will be overridden and not propagated to
        // _executeCloseAction, as there wasn't any plan to re-open record,
        // originally. So here we check for the 'o_btn_keep_open' and will
        // make a backup of both attrs/record data.

        if (_.has(ev.data.attrs, 'class')) {
            // check for one of two class selctors and save reference
            var mode = '';

            if (ev.data.attrs.class.includes('o_btn_keep_open')) {
                mode = 'o_btn_keep_open';
            }

            else if (ev.data.attrs.class.includes('o_btn_reopen')) {
                mode = 'o_btn_reopen';
            }

            if (mode === 'o_btn_reopen' || mode === 'o_btn_keep_open') {

                // We need to bind on ev.data.attrs to make sure data will be propagated
                ev.data.attrs.keep_dialog_active = Object.assign({}, ev.data);

                // Also retrieve from instance few datas that would not be mapped by default
                var view_id = false;

                // try to retrieve view_id to reload specific view in case of a specific view_id
                if (_.has(this, 'viewId') && this.viewId){
                    view_id = this.viewId;
                } else if (_.has(this, 'actionViews') && this.actionViews && _.has(this.actionViews[0], 'viewID')) {
                    //fallback if no renderer. I'm almost sure this is an overkill (remove?)
                    view_id = this.actionViews[0].viewID;
                }

                ev.data.attrs.keep_dialog_active.additionalData = {

                    title: this._title, // to restore title of the window
                    selector_mode: mode,
                    viewID: view_id,
                }
            }
        }
        return this._super.apply(this, arguments);
    },

    /*
     * Intercepts updated attrs/record params and updates
     * action data backup after saveRecord is called:
     * when we create 'keep_dialog_active' res_id is not yet
     * available in pseudo-records.
     */
    _callButtonAction: function (attrs, record) {
        if (_.has(attrs, 'keep_dialog_active')){
            attrs.keep_dialog_active.record = record;
            attrs.keep_dialog_active.attrs = attrs;
        }
        // MUST "return" here, or UI raise def undefined in some case
        // (e.g. click on footer close btn after exec)..see saveAndExecuteAction
        return this._super.apply(this, arguments);
    },

});

});
