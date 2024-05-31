odoo.define("listview_make_all_fields_optional.ListRenderer", function (require) {
    "use strict";

    var ListRenderer = require("web.ListRenderer");

    ListRenderer.include({
        _processColumns: function (columnInvisibleFields) {
            _.each(
                this.arch.children.filter((fields) => fields.tag == "field"),
                function (node) {
                    if (node.attrs.optional !== "hide") {
                        node.attrs.optional = "show";
                    }
                }
            );
            this._super.apply(this, arguments);
        },
    });
});
