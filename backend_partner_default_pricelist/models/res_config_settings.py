from odoo import api, fields, models

DP_PARAM = "backend_partner_default_pricelist.backend_pricelist_default_id"


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    backend_pricelist_default_id = fields.Many2one(
        comodel_name="product.pricelist", string="Default Pricelist: backend"
    )

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "backend_partner_default_pricelist.backend_pricelist_default_id",
            self.backend_pricelist_default_id.id,
        )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        backend_pricelist_default_id = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("backend_partner_default_pricelist.backend_pricelist_default_id")
        )
        res.update(backend_pricelist_default_id=int(backend_pricelist_default_id))
        return res
