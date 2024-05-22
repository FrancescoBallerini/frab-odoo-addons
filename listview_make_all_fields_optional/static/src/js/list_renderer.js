odoo.define("listview_make_all_fields_optional.ListRenderer", function (require) {
    "use strict";

    var ListRenderer = require("web.ListRenderer");

    ListRenderer.include({
        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                _.each(
                    self.arch.children.filter((fields) => fields.tag == "field"),
                    function (node) {
                        if (node.attrs.optional !== "hide") {
                            node.attrs.optional = "show";
                        }
                    }
                );
            });
        },
    });
});
