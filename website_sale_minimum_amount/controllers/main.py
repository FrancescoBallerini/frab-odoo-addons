import datetime

from odoo.addons.website_sale.controllers.main import WebsiteSale as WebsiteSale
from odoo.http import request


class WebsiteSaleMinimumAmount(WebsiteSale):
    def checkout_redirection(self, order):
        if order:
            # check order to avoid AssertionError in _convert()
            # when there is no active order
            order_amount = (
                order.amount_untaxed
                if request.website.website_sale_min_amount_type == "tax_excluded"
                else order.amount_total
            )
            if order.currency_id and order.company_id.currency_id:
                # avoid AssertionError in _convert() in every possible situation
                required_amount = order.currency_id._convert(
                    from_amount=request.website.website_sale_min_amount,
                    to_currency=order.company_id.currency_id,
                    company=order.company_id,
                    date=datetime.date.today(),
                    round=False,
                )
            else:
                required_amount = request.website.website_sale_min_amount

            skip_check = request.env.context.get("bypass_minimum_amount_check")

            if not skip_check and order_amount < required_amount:
                return request.redirect("/shop/cart")

        return super(WebsiteSaleMinimumAmount, self).checkout_redirection(order=order)
