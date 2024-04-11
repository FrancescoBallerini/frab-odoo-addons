from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    seller_ids_group_by = fields.Char(
        compute="_compute_seller_ids_group_by", store=True
    )

    @api.depends("seller_ids")
    def _compute_seller_ids_group_by(self):
        # groupby workaround: create a computed field storing
        # a string containing mapped() of seller names. This
        # hack is needed in order to allow groupby on o2m/m2m
        for product in self:
            sellers = (
                product.seller_ids.mapped("name") or ""
            )  # this "name" is actually a `res.partner` id
            sellers_formatted = " ///// ".join([seller.name for seller in sellers])
            product.seller_ids_group_by = sellers_formatted
