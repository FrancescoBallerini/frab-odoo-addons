from odoo import http
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website_sale.controllers.main import TableCompute, WebsiteSale
from odoo.http import request


class WebsiteSaleSortByPricelistPrice(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        response = super(WebsiteSaleSortByPricelistPrice, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
        order = post.get("order")
        if order and any(
            sortby_filter in order
            for sortby_filter in ["sortby_price_asc", "sortby_price_desc"]
        ):
            Product = search_product = request.env["product.template"].with_context(
                bin_size=True
            )
            attrib_values = response.qcontext.get("attrib_values", [])
            domain = self._get_search_domain(
                search=search, category=category, attrib_values=attrib_values
            )
            # if `sortby_price_asc` or `sortby_price_desc` filter is found in post execute
            # the patched ORM search() which will done a sortby in python instead of using ORM.
            # See Base module ProductTemplate.search() implementation.
            if "sortby_price_asc" in order:
                search_product = Product.with_context(sortby_price_asc=True).search(
                    domain
                )
            elif "sortby_price_desc" in order:
                search_product = Product.with_context(sortby_price_desc=True).search(
                    domain
                )
            # we have ordered products: need to update the offset. The following code request
            # a new pager, update the offset and update qweb context for the render
            url = "/shop"
            category = response.qcontext.get("category")
            if category:
                url = "/shop/category/%s" % slug(category)
            product_count = len(search_product)
            ppg = response.qcontext.get("ppg")
            ppr = response.qcontext.get("ppr")
            pager = request.website.pager(
                url=url,
                total=product_count,
                page=page,
                step=ppg,
                scope=5,
                url_args=post,
            )
            offset = pager["offset"]
            products = search_product[offset : offset + ppg]
            # Update qweb render values:
            # TableCompute().process(...) also needs to be called otherwise the grid will not be updated
            response.qcontext.update(
                {
                    "products": products,
                    "bins": TableCompute().process(products, ppg, ppr),
                }
            )
        return response
