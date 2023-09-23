from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route


class WebsiteSaleLocationAutocomplete(WebsiteSale):
    @route("/shop/address/get_zipcode_autocomplete_source", type="json", auth="user")
    def get_zipcode_autocomplete_source(self, country_id):

        """Call this function:
         - after `start()` of widget `WebsiteSaleZipcodeAutocomplete`
         - when frontend user change the selected `country_id`

        :param int country_id: `id` of selected country when this :meth: is called

        :return dict: the dictionary to use as `source` param for ui-autocomplete

        Ref: https://api.jqueryui.com/autocomplete/"""

        autocomplete_source = self._zipcode_autocomplete_process_data(country_id)
        return {
            "autocomplete_source": autocomplete_source,
        }

    @route("/shop/address/on_submit_zipcode_autocomplete", type="json", auth="user")
    def on_submit_zipcode_autocomplete(self, selected_res_city_zip_id):

        """Set `zip_id` field on backend with a different controller
        to bypass `details_form_validate`: there is no need to
        validate this field since it's value is a consequence of
        user choice on `zipcode` input, so we call `write` to avoid
        loading huge number of zip records on html.

        Despite skipping controller validation the `write` has to be
        done on Submit to ensure data consistency."""

        user = request.env.user
        partner_id = user.partner_id
        partner_id.sudo().write({"zip_id": selected_res_city_zip_id})

    def _zipcode_autocomplete_process_data(self, country_id):
        # filter the source based on selected `country_id`
        zipcodes = (
            request.env["res.city.zip"].sudo().search([("country_id", "=", country_id)])
        )
        if not zipcodes:
            return []
        jq_autocomplete_source = [
            {"label": z.display_name, "value": z.name} for z in zipcodes
        ]
        return jq_autocomplete_source
