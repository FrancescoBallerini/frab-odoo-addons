odoo.define("website_sale_sort_by_refresh.website_sale", function (require) {
    "use strict";

    var core = require("web.core");
    var publicWidget = require("web.public.widget");

    require("website_sale.website_sale");

    publicWidget.registry.WebsiteSale.include({
        start() {
            const def = this._super(...arguments);
            // In order to reset the Sort By query we remove all 'order' params
            // from anchors href in the body unless. Some anchors actually need
            // to keep the param to perform the orderby e.g. the Sort Button
            // and pager items: skip them with a class selector
            $("body a").each(function (index, anchor) {
                if (anchor.href && !$(anchor).hasClass("skip_sort_by_refresh")) {
                    var anchor_url = new URL(anchor.href);
                    if (
                        anchor_url.pathname.includes("/shop") &&
                        anchor_url.searchParams.get("order")
                    ) {
                        var new_anchor_url = anchor_url;
                        new_anchor_url.searchParams.delete("order");
                        anchor.href = new_anchor_url.href;
                    }
                }
            });
            return def;
        },
    });
});
