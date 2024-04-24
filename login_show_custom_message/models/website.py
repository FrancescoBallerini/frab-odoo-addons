from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    login_custom_message = fields.Html(translate=True)
    signup_custom_message = fields.Html(translate=True)
