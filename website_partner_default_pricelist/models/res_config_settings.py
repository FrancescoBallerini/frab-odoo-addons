from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    website_pricelist_default_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Default Pricelist: e-Commerce",
        related="website_id.website_pricelist_default_id",
        readonly=False,
    )
