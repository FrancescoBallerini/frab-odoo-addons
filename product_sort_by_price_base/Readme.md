# Product Sort By Price (Base)

In odoo14 is only possible to sort by `Sales Price` field, which is a fixed value for
the customer prices. This module makes possible to sort by `Price`, which is the price
field having pricelist items compatibility. Please note that this is the Base module: in
order to make it work in applications (e.g.
[e-Commerce](https://github.com/FrancescoBallerini/odoo14_custom_modules/website_sale_sort_by_pricelist_price))
you need to install the specific extension.

## Technical description

The behaviour of sortby for `Price` is essentially not available due to ORM limitations
with non-stored computed fields (check
[#27743](https://github.com/odoo/odoo/issues/27743) for more info).

This module extends the ORM search() for ProductTemplate model and will check for two
context-keys:

- `sortby_price_asc`
- `sortby_price_desc`

you inject in the context one of these keys in order to retrieve the product sorted by
price asc or desc,

E.g.

`self.env['product.template'].with_context(sortby_price_asc=True).search([])`

will retrieve all product templates sorted by ascendant price.

The sortby is done inside the search() with a simple pure python dictionary sorting,
bypassing the ORM limitations with non-stored fields.

## Roadmap

- compatibility with product variant prices
