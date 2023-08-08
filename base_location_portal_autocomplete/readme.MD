## Description

This module allows Portal Details FormView to automatically fill


- the `state_id` select
- the `city` input

by selecting a city from a dropdown menu that will appear on the `zipcode` input.

![autocomplete_example.gif](static%2Fsrc%2Fimg%2Fautocomplete_example.gif)

## Usage/Configuration

Module installation will automatically enable dropdown menu. However, to display the dropdown you need 
to store entities (records) representing cities for the selected country.


Don't worry: you can easily configure your database in a few step and store all the cities for 
desired countries, by installing [base_location_geonames_import](https://github.com/OCA/partner-contact/tree/14.0/base_location_geonames_import). It will allow you to
automatically import records for countries of your choice.

However, if for any reason you only need to display limited records you are allowed to configure cities
manually and only install [base_location](https://github.com/OCA/partner-contact/tree/14.0/base_location): in fact, this module does not technically 
require for [base_location_geonames_import](https://github.com/OCA/partner-contact/tree/14.0/base_location_geonames_import) to be installed, so it will work properly if 
you only install the former. If that's the case and you need to manually configure cities on
your database, you could take a look at the [module usage](https://github.com/OCA/partner-contact/tree/14.0/base_location#usage).

---
Once you have configured your database with cities, either manually or by importing them as
explained above: 

* Access to your account details: this is generally achieved by logging and clicking on "My account", 
then clicking on "Details". However, this step might differ if you installed third party modules, 
expecially themes.


* Once you reached Portal "Details" Form-View, select any country


* If selected country has city records to show, it will display them in the dropdown
  

* Click on any auto-complete item to automatically fill city and state


## Notes

* Dropdown menu will appear on the third digit input. At the moment there is no GUI option to
change this behaviour, it has to be done from code.


* Dropdown menu is loaded on GUI by making usage of jquery-ui library integrated in the odoo14 framework. 
For browser compatibility you can check library version [here](https://github.com/odoo/odoo/blob/14.0/addons/web/static/lib/jquery.ui/jquery-ui.js).




