## Description

This module allows to set a default pricelist in the pricing settings menu: chosen
pricelist will be selected by default on the form-view when creating a new partner in
backend.

Before installing this module you must rely on the sequence of the pricelists view (the
first pricelist will be taken as default). Not only is this dangerous but it also
doesn't let you define different choices between backend and e-Commerce.

Check
[website_partner_default_pricelist](https://github.com/FrancescoBallerini/frab-odoo-addons/tree/main/website_partner_default_pricelist)
for the same feature in front-end side.

## Configuration

- Settings > Pricing

- Search for "Default Pricelist: backend" dropdown and simply select the default
  pricelist.

## Notes

- Not optimized for multi-company environment
