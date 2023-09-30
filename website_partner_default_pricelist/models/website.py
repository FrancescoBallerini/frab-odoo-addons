from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    def _default_pricelist_id(self):
        return self.env["product.pricelist"].search(
            ["|", ("company_id", "=", False), ("company_id", "=", self.env.company.id)],
            limit=1,
        )

    website_pricelist_default_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Default Pricelist: e-Commerce",
        default=_default_pricelist_id,
    )
