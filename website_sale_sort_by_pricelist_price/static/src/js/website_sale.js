odoo.define("website_sale_sort_by_pricelist_price.website_sale", function (require) {
    "use strict";

    var publicWidget = require("web.public.widget");
    require("website_sale.website_sale");

    publicWidget.registry.WebsiteSale.include({
        /**
         * @override
         */
        start() {
            // replace list_price+asc / desc href with dummy fields
            // Done in JS so we don't override Qweb SortBy Template
            const def = this._super(...arguments);
            var hyperlinksDropdown = this.$(".sorty_by_dropdown_hyperlinks");
            if (hyperlinksDropdown.length) {
                var hyperlinks = hyperlinksDropdown.children();
                _.each(hyperlinks, function (hyperlink) {
                    if (hyperlink.href.includes("order=list_price+asc")) {
                        var hrefUpdate = hyperlink.href.replace(
                            "list_price+asc",
                            "sortby_price_asc"
                        );
                        hyperlink.href = hrefUpdate;
                    } else if (hyperlink.href.includes("order=list_price+desc")) {
                        var hrefUpdate = hyperlink.href.replace(
                            "list_price+desc",
                            "sortby_price_desc"
                        );
                        hyperlink.href = hrefUpdate;
                    }
                });
            }
            return def;
        },
    });
});
