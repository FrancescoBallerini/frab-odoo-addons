from odoo import api, fields, models
from odoo.osv.expression import AND


class City(models.Model):
    _inherit = "res.city"

    nuts3_id = fields.Many2one(
        comodel_name="res.partner.nuts",
        domain="[('id', 'in', allowed_nut_ids)]",
        string="NUTS L3",
    )

    allowed_nut_ids = fields.Many2many(
        comodel_name="res.partner.nuts",
        string="Allowed nuts",
        compute="_compute_allowed_nuts",
    )

    @api.depends("country_id")
    def _compute_allowed_nuts(self):
        Nuts = self.env["res.partner.nuts"]
        for city in self:
            domain = [("level", "=", 3)]
            if city.country_id:
                domain = AND(
                    [
                        domain,
                        [
                            ("country_id", "=", city.country_id.id),
                            (
                                "name",
                                "!=",
                                "Extra-Regio NUTS 2",
                            ),  # exclude dirty records from regions
                        ],
                    ]
                )
            city.allowed_nut_ids = Nuts.search(domain)
