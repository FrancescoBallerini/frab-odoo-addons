from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    website_sale_min_amount = fields.Monetary(
        string="Website Sale Minimum Amount",
        related="website_id.website_sale_min_amount",
        readonly=False,
    )

    website_sale_min_amount_type = fields.Selection(
        string="Minimum Amount Type",
        related="website_id.website_sale_min_amount_type",
        readonly=False,
    )
