import datetime

from odoo.addons.website_sale.controllers.main import WebsiteSale as WebsiteSale
from odoo.http import request


class WebsiteSaleMinimumAmount(WebsiteSale):
    def checkout_redirection(self, order):

        order_amount = (
            order.amount_untaxed
            if request.website.website_sale_min_amount_type == "tax_excluded"
            else order.amount_total
        )

        required_amount = order.pricelist_id.currency_id._convert(
            from_amount=request.website.website_sale_min_amount,
            to_currency=order.company_id.currency_id,
            company=order.company_id,
            date=datetime.date.today(),
            round=False,
        )

        if order_amount < required_amount:
            return request.redirect("/shop/cart")

        return super(WebsiteSaleMinimumAmount, self).checkout_redirection(order=order)
