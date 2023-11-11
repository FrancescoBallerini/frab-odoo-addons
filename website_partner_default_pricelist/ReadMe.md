## Description

This module allows to set a default pricelist for e-Commerce customers.

Selected pricelist will be assigned by default to new customers when they signup on your
website (only b2c: check
[Usage](https://github.com/FrancescoBallerini/odoo14_custom_module_private/tree/main/website_partner_default_pricelist#usage)
section for more info).

Before installing this module you must rely on the sequence of the pricelists view (the
first pricelist will be taken as default). Not only is this dangerous but it also
doesn't let you define different choices between backend and e-Commerce.

Check
[backend_partner_default_pricelist](https://github.com/FrancescoBallerini/odoo14_custom_modules/tree/main/backend_partner_default_pricelist)
for the same feature in the backend side.

## Configuration

- General Settings > Website

- In case you manage more than one website be sure that you selected the right one in
  General Settings menu. You can also manage this setting by navigating to Website
  Menus > Configuration and selecting a specific website (it's equivalent).

- Once you selected a website, Search for "Default Pricelist: e-Commerce" dropdown and
  simply select the default pricelist for selected website.

## Usage

### Public Users (not impacted)

Not impacted by module: non-logged users still display prices accordingly to Public
Partner's pricelist.

### B2C: Free Signup (impacted)

B2C signup is impacted by module behaviour: selected default pricelist will be set on
the Partner as soon as he completes the signup.

### B2B: on invitation (not impacted)

Not impacted by module: when giving portal access by sending an invitation, contacts'
Pricelist will NOT be overridden.
