## Description

Before installing this module if you need to set a Default Pricelist for new partners
you must to rely on Pricelist model sequence. That means that you have to place your
Pricelist on the top of "Pricelists" view and hope for the best.

This module allows to set a Default Pricelist in the Website Settings menu: selected
pricelist will be selected by default when a new Customer signup on your website.

## Configuration

- Enable "Pricelists" flag in case it's not active. You can find it on section
  Settings > Pricing.

- Find section General Settings > Website.

- In case you manage more than one website, be sure that you selected the right one in
  General Settings menu. You can also manage this setting by navigating to Website >
  Configuration and selecting a website.

- Once you selected a website, Search for "Default Pricelist: e-Commerce" dropdown and
  simply select the default pricelist for selected website.

## Usage

### B2C: Free Signup - Public Users

This module does not impact "Public Partner" pricelist, this means that non-logged users
will display prices accordingly to "Public Partner" pricelist. In case you allow Public
Users to make order and submit address from checkout, it's worth mentioning that default
selected pricelist will be assigned, BUT only after they make the first login. In order
to properly manage this workflow, you might want to manually re-assign pricelist on the
"Public User", to align it with e-Commerce default pricelist defined in Website
Settings.

### B2C: Free Signup - Logged Users

Selected pricelist will be set on the Partner as soon as he completes the signup.

### B2B: on invitation

When you give Portal Access to a contact from backend the Pricelist will NOT be
overridden by e-Commerce default pricelist.
