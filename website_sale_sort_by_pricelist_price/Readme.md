# Website Sale: Sort By Pricelist Price

In odoo14 e-Commerce it's not possible to sort by pricelist price: the Sort By button
only allows to sort by `Sales Price`, which is a fixed value for the customer prices.
This module allows to sort by `Price`, which is the price field having pricelist items
compatibility.

## Usage

- The installation of this module will automatically enable the compatibility with
  `Pricelist Price` when using Sort By Button on the e-Commerce.

- Sort By Button will prioritize the `Pricelist Price` over `Sales Price`. However, if
  some products are configured by only having a static `Sales Price` and no
  `Pricelist Price` (no pricelist rule matching the product for the active pricelist)
  those products will still be correctly ordered as if the `Sales Price` was the
  `Pricelist Price` in this case.

- If you manage an e-Commerce with thousands of products some Sort By queries (e.g.
  categories storing about 1000+ products) might be really taxing for performance when
  sorting by `Pricelist Price`. This is not really an issue that we can solve directly,
  but you might be interested into this module as well as a partial workaround:
  [website_sale_sort_by_refresh](https://github.com/FrancescoBallerini/frab-odoo-addons/website_sale_sort_by_refresh)

## Roadmap

- compatibility with product variant prices
