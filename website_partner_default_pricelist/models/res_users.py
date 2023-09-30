from odoo import api, models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def _signup_create_user(self, values):
        current_website = self.env["website"].get_current_website()
        pricelist_id = current_website.website_pricelist_default_id
        if pricelist_id:
            values.update(
                {
                    "property_product_pricelist": pricelist_id.id,
                }
            )
        new_user = super(ResUsers, self)._signup_create_user(values)
        return new_user
