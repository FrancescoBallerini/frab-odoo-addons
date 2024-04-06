from odoo import http
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website_sale.controllers.main import TableCompute, WebsiteSale
from odoo.http import request

SORT_BY_PRICE_ASC_KEYS = ["list_price asc"]
SORT_BY_PRICE_DESC_KEYS = ["list_price desc"]
SORT_BY_PRICE_KEYS = SORT_BY_PRICE_ASC_KEYS + SORT_BY_PRICE_DESC_KEYS


class WebsiteSaleSortByPricelistPrice(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        response = super(WebsiteSaleSortByPricelistPrice, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
        # check if an "order by price" has been requested
        sort_by_option = post.get("order") or request.params.get("order")
        if sort_by_option and sort_by_option in SORT_BY_PRICE_KEYS:
            # Make another search() that will override the recordset of the first
            # search based on `list_price`: this search() will receive the `order`
            # param by context, which will specify the sort type (asc/desc) if a
            # price sorting option has been selected.
            # The ORM method ProductTemplate.search() has been patched so it will
            # execute a python sort by (instead of ORM sort by) when receiving
            # one of these keys
            Product = request.env["product.template"].with_context(bin_size=True)
            attrib_values = response.qcontext.get("attrib_values", [])
            domain = self._get_search_domain(
                search=search, category=category, attrib_values=attrib_values
            )
            sort_by_option_propagation = {sort_by_option: True}
            # propagate `request.env.context` as well as it's contains active pricelist ID
            search_product = Product.with_context(
                request.env.context, **sort_by_option_propagation
            ).search(domain)
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
