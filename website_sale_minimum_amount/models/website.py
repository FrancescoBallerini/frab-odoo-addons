from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    website_sale_min_amount = fields.Float(string="Website Sale Minimum Amount")

    website_sale_min_amount_type = fields.Selection(
        string="Minimum Amount Type",
        selection=[("tax_included", "Tax included"), ("tax_excluded", "Tax excluded")],
    )
