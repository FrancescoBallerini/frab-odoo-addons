## Description

This module adds Many2one reference for NUTS3 on 'res.city' model: it might be useful to
have an reference on the model to avoid queries on 'res.city' and 'res.partner.nuts'
when you want to associate a NUTS3 record to a city or even a zip if you installed
module such as
https://github.com/OCA/partner-contact/tree/14.0/base_location_geonames_import.

This module also has an automatic synchronization for cities and NUTS3, which is kept at
minimal implementation and has some requirements. See "USAGE" section for info about
automatic sync.

## Usage

Sync requirements:

Sync requirement are summarized below

1- downloaded NUTS data from
https://github.com/OCA/partner-contact/tree/14.0/base_location_nuts

2- you should already have mapped NUTS level 4 with state_id, manually or via import

for more info about step 2, install the module click on menu
"Contacts/Configuration/Cities-NUTS3 Synchronization", then click on "info" button: the
wizard will show a detailed explanation of requirements and "info" button will give some
hints to achieve auto-sync between cities and NUTS3 records.
