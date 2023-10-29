from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale as WebsiteSale
from odoo.http import request


class WebsiteSaleProductSearchPrefetch(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, brand=None, ppg=False, search="", **post):
        if search:
            # enable prefetch on /shop when searching for a product
            ctx = request.context
            request.context = dict(ctx, product_code_prefetch=True)
        return super(WebsiteSaleProductSearchPrefetch, self).shop(
            page=page, category=category, brand=brand, search=search, **post
        )

    @http.route()
    def products_autocomplete(self, term, options={}, **kwargs):
        if term:
            # enable prefetch for product preview on autocomplete snippet
            ctx = request.context
            request.context = dict(ctx, product_code_prefetch=True)
        return super(WebsiteSaleProductSearchPrefetch, self).products_autocomplete(
            term=term, options=options, kwargs=kwargs
        )
