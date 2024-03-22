from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def _update_and_sortby_computed_price(self, product_templates, reverse):

        """Sort by is done by python dictionary:
        a `dict` {product_id: product_price} will be created then sorted by
        values (prices) and reversed if `sortby_price_desc`. Records will
        be re-browsed with dictionary order and since browse is keeping the
        order the recs are returned sorted by price"""

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
        res = super(ProductTemplate, self).search(
            args, offset=offset, limit=limit, order=order, count=count
        )
        if self.env.context.get("sortby_price_asc"):
            res = self._update_and_sortby_computed_price(
                product_templates=res, reverse=False
            )
        elif self.env.context.get("sortby_price_desc"):
            res = self._update_and_sortby_computed_price(
                product_templates=res, reverse=True
            )
        return res
