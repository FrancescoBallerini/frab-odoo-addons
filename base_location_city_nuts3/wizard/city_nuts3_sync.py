from odoo import models, fields, _


class CityNuts3Sync(models.TransientModel):
    _name = 'city.nuts3.sync'
    _description = "Import City-NUTS3 reference via csv"

    show_step3_hints = fields.Boolean(default=False)

    def click_step_3_hints(self):

        if self.show_step3_hints:
            self.show_step3_hints = False
        else:
            self.show_step3_hints = True

        return {
            'name': _('Cities/NUTS3 Synchronization'),
            'res_model': 'city.nuts3.sync',
            'view_mode': 'form',
            'context': self.env.context,
            'target': 'new',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
        }

    def run_city_nuts3_sync(self):
        cities = self.env['res.city'].search([]).sorted(key=lambda c: (c.country_id.id, c.state_id.id))
        # only keep NUTS data related to cities
        city_country_ids = [city.country_id.id for city in cities]
        country_nuts_ids = self.env['res.partner.nuts'].search(
            [
                ('level', '=', 4),
                ('country_id', 'in', city_country_ids)
            ]
        )
        for city in cities:
            city.nuts3_id = country_nuts_ids.filtered(
                lambda nuts: nuts.state_id.id == city.state_id.id
            ).parent_id.id
