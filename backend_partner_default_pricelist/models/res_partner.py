from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def default_get(self, fields_list):
        defaults = super(ResPartner, self).default_get(fields_list)
        IrConfig = self.env["ir.config_parameter"]
        backend_pricelist_default_id = IrConfig.sudo().get_param(
            "backend_partner_default_pricelist.backend_pricelist_default_id"
        )
        if backend_pricelist_default_id:
            defaults["property_product_pricelist"] = int(backend_pricelist_default_id)
        return defaults
