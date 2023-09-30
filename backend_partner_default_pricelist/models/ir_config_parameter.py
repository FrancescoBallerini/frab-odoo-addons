from odoo import _, api, models
from odoo.exceptions import ValidationError

DP_PARAM = "backend_partner_default_pricelist.backend_pricelist_default_id"


class IrConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    @api.model_create_multi
    def create(self, vals_list):

        """This parameter must only be written/created from `res.config.settings` model:
        it will be automatically stored as `int` compatible value (a non-integer fetch
        on a many2one record will cause GUI crash on settings load). Another reason is
        on `res.config.settings` user will only be able to select records related to
        his company, so it's more compatible with multi-company environment checks."""

        ctx = self.env.context
        create_from_settings = (
            ctx.get("params", {}).get("model") == "res.config.settings"
            or ctx.get("module") == "general_settings"
        )
        if not create_from_settings:
            for vals in vals_list:
                for key in vals.keys():
                    if key == DP_PARAM:
                        raise ValidationError(
                            _(
                                "Cannot set from System Parameters. You should select "
                                "the default pricelist from Pricing Settings."
                            )
                        )
        return super().create(vals_list)

    def write(self, values):

        """This parameter must only be written/created from `res.config.settings` model:
        it will be automatically stored as `int` compatible value (a non-integer fetch
        on a many2one record will cause GUI crash on settings load). Another reason is
        on `res.config.settings` user will only be able to select records related to
        his company, so it's more compatible with multi-company environment checks."""

        ctx = self.env.context
        create_from_settings = (
            ctx.get("params", {}).get("model") == "res.config.settings"
            or ctx.get("module") == "general_settings"
        )
        if not create_from_settings:
            for kv_param in self:
                if kv_param.key == DP_PARAM:
                    raise ValidationError(
                        _(
                            "Cannot set from System Parameters. You should select "
                            "the default pricelist from Pricing Settings."
                        )
                    )
        return super().write(values)
