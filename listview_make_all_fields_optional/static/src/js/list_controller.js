odoo.define("listview_make_all_fields_optional.ListController", function (require) {
    "use strict";

    var ListController = require("web.ListController");

    ListController.include({
        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                var state = self.model.get(self.handle);
                self.renderer.updateState(state, {
                    reload: true,
                });
            });
        },
    });
});
