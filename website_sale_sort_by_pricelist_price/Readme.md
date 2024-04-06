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

## Roadmap

- compatibility with product variant prices
