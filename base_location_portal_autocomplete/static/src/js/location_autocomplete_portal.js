odoo.define("base_location_portal_autocomplete.portal_extend", function (require) {
    "use strict";

    var core = require("web.core");
    var config = require("web.config");
    var publicWidget = require("web.public.widget");
    require("portal.portal");

    publicWidget.registry.portalZipcodeAutocomplete = publicWidget.Widget.extend({
        selector: ".portal_zipcode_autocomplete",

        events: {
            'change select[name="country_id"]': "_onCountryChange",
            "submit .portal_form_submit": "_onSubmit",
        },

        init: function () {
            this._super.apply(this, arguments);
            this.selected_res_city_zip_id = false;
        },

        /**
         * @Override:
         * Fetch proper source and load autocomplete if source is found
         * for selected country. Sources are 'res.city.zip' records
         * attached to selected country.
         */
        start: function () {
            var def = this._super.apply(this, arguments);
            this._updateZipcodeAutocompleteUI();
            return def;
        },

        //--------------------------------------------------------------------------
        // Handlers
        //--------------------------------------------------------------------------

        /**
         * Country change:
         * Re-fetching the source and rebuild autocomplete or destroy it
         * if there is no source (res.city.zip) for selected country.
         */
        _onCountryChange: function (ev) {
            this._updateZipcodeAutocompleteUI();
        },

        /**
         * Manage UI-autocomplete events after an item has been focused.
         */
        _setZipcodeAutocompleteValues: function (event, ui) {
            // ui.item.value/ui.item.label are updated each
            // time user select a "source item".
            // This generally happen with a "click" on an
            // autocomplete item or other events (like arrow down
            // after ui-autocomplete pops-up). We could manage
            // "change" event as well and make some "fallback
            // shenanigans" to retrieve, let's say only state_id
            // instead of cities when user insert a valid zipcode
            // without focusing the widget, but for now we limit
            // to case when ui.item is not null.
            if (ui.hasOwnProperty("item") && ui.item != null) {
                // Make an rpc by matching selected "label" with
                // "display_name" to retrieve other fields from city
                var self = this;
                var prom = this._rpc({
                    model: "res.city.zip",
                    method: "search_read",
                    kwargs: {
                        domain: [["display_name", "=", ui.item.label]],
                        limit: 1,
                        fields: ["display_name", "city_id", "state_id"],
                    },
                }).then(function (result) {
                    var self2 = self;
                    if (Object.keys(result).length > 0) {
                        // fill "state_id" and "city_id" on form-view
                        $("select[name='state_id']").val(result[0].state_id[0]);
                        $("input[name='city']").val(result[0].city_id[1]);
                        if (result[0].hasOwnProperty("id")) {
                            // store the 'res.city.zip' record, we need it on submit
                            // to set zip_id rec on 'res.partner' backend.
                            self2.selected_res_city_zip_id = result[0].id;
                        }
                    }
                });
                return prom;
            }
        },

        /**
         *  Set "zip_id" field on backend with a different controller
         *  to bypass "details_form_validate()": there is no need to
         *  validate this field since it's value is a consequence of
         *  user choice on "zipcode" input, so we call write() to avoid
         *  loading huge number of zip records on html.
         *  Despite skipping controller validation this query has to be
         *  done on Submit (when all form fields passed validation) in
         *  order to ensure data consistency in case of transaction rollback.
         */
        _onSubmit: function (ev) {
            var self = this;
            var def = this._super.apply(this, arguments).then(function (r) {
                self._rpc({
                    route: "/my/account/on_submit_zipcode_autocomplete",
                    params: {
                        selected_res_city_zip_id: self.selected_res_city_zip_id,
                    },
                });
            });
            return def;
        },

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * Call method to update source, then manage ui-autocomplete:
         * if a source length is returned, build the ui-autocomplete,
         * else destroy it, in case it was active before.
         */
        _updateZipcodeAutocompleteUI: function () {
            var country_id = parseInt($("select[name='country_id']").val());
            var self = this;
            // update source
            this._updateZipcodeAutocompleteSource(country_id).then(function (
                sourceList
            ) {
                if (Object.keys(sourceList).length > 0) {
                    var position = {collision: "flip"};
                    var minLength = 3;
                    if (config.device.isMobile || config.device.isMobileDevice) {
                        // on small screen avoid covering input while user still typing
                        // isMobile true when screen-size: XS/VSM/SM
                        minLength = 5;
                    }
                    // append autocomplete to zipcode input
                    $("input[name='zipcode']").autocomplete({
                        source: sourceList,
                        minLength: minLength,
                        position: position,
                        select: function (event, ui) {
                            // set vals in form-view on item select
                            self._setZipcodeAutocompleteValues(event, ui);
                        },
                    });
                } else if ($("input[name='zipcode']").autocomplete("instance")) {
                    $("input[name='zipcode']").autocomplete("destroy");
                }
            });
        },

        /**
         * Get autocomplete source by calling python controller
         */
        _updateZipcodeAutocompleteSource: function (countryID) {
            var def = this._rpc({
                route: "/my/account/get_zipcode_autocomplete_source",
                params: {
                    country_id: countryID,
                },
            }).then(function (result) {
                return result.autocomplete_source;
            });
            return def;
        },
    });
});
