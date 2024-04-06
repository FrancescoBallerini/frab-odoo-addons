from odoo import api, models
from odoo.addons.website_sale_sort_by_pricelist_price.controllers.main import (
    SORT_BY_PRICE_ASC_KEYS,
    SORT_BY_PRICE_DESC_KEYS,
)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def _update_and_sortby_computed_price(self, product_templates, reverse):
        """Retrieve computed price and perform a python sort by:
        a `dict` {product_id: product_price} will be created then sorted by
        values (prices) and reversed if `list_price desc` key is the one
        that has been propagated in the context. Records will then be browsed
        by fetching dictionary keys (which are product ids ordered by price)
        and since browse will keep the order we can return the recordset of
        products sorted by price"""
        product_prices = {}
        for product in product_templates:
            product_prices.update({product.id: product.price})
        sorted_product_prices = dict(
            sorted(product_prices.items(), key=lambda kv: kv[1], reverse=reverse)
        )
        sorted_product_prices_ids = [k for k, v in sorted_product_prices.items()]
        product_templates_sorted = self.browse(sorted_product_prices_ids)
        return product_templates_sorted

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """Patch search method so it will execute a sortby in python when
        receiving an e-Commerce sortby key from the Sort By button"""
        res = super(ProductTemplate, self).search(
            args, offset=offset, limit=limit, order=order, count=count
        )
        if any(key in self.env.context for key in SORT_BY_PRICE_ASC_KEYS):
            res = self._update_and_sortby_computed_price(
                product_templates=res, reverse=False
            )
        elif any(key in self.env.context for key in SORT_BY_PRICE_DESC_KEYS):
            res = self._update_and_sortby_computed_price(
                product_templates=res, reverse=True
            )
        return res
