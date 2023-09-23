## Description

This module allows Checkout Address Form-View to automatically fill


- `state` select
- `city` input

by selecting a city from a dropdown menu that will appear on the `zipcode` input.

![autocomplete_example.gif](static%2Fsrc%2Fimg%2Fautocomplete_example.gif)

## Configuration

Module installation will automatically enable dropdown menu. However, to display the dropdown you need
to store entities (records) representing cities for the selected country.


Don't worry: you can easily configure your database in a few step and store all the cities for
desired countries by installing [base_location_geonames_import](https://github.com/OCA/partner-contact/tree/14.0/base_location_geonames_import). It will allow you to
automatically import records for countries of your choice.

If for any reason you only need to display limited records you are allowed to configure cities
manually and only install [base_location](https://github.com/OCA/partner-contact/tree/14.0/base_location): installation of [base_location_geonames_import](https://github.com/OCA/partner-contact/tree/14.0/base_location_geonames_import)
is not required for this module (only [base_location](https://github.com/OCA/partner-contact/tree/14.0/base_location) is).

## Usage
Once you have properly configured your DB, Checkout Address Form-View will have new feature:

- when a user fill `zipcode` input a dropdown will be shown: displayed values are cities sharing
the zipcode input, based on selected country


- click on a city to automatically fill `state` and `city` fields


## Notes

* Dropdown menu will appear on the third digit input. At the moment there is no GUI option to
change this behaviour, it has to be done from code.


* Dropdown menu is loaded on GUI by making usage of jquery-ui library integrated in the odoo14 framework.
For browser compatibility you can check library version [here](https://github.com/odoo/odoo/blob/14.0/addons/web/static/lib/jquery.ui/jquery-ui.js).
