## Description

This module will improve product search by Internal Reference (product code) for most
common backend and e-Commerce views.

This is really helpful when you have a lot of products and you or your customers usually
search product by code instead of name: in Odoo the Internal Reference is evaluated when
you make a search, on product name but the result is too inclusive and if you have a lot
of product matching the "search" you might not actually be able to filter products
properly.

#### A very simple example:

- Product 1: Name "LED X12A1"
- Product 2: Internal Reference "A11"
- Product 3: Internal Reference "A1"
- Product 4: Internal Reference "BH_A1"
- Product 5: Internal Reference "A1135"

#### Before installing the module:

In e-Commerce search or backend searchview by name, if you type "A1" and you match all
of these products

This can become an issue when you have a lot of products that matches the search
pattern, as you and your customers might receive full pages of matching products and
take very small benefit from the filtered search.

#### After module installation:

In e-Commerce search or backend searchview by name, if you type "A1" you will only find
product 3.

#### How the check works, specifically:

- if ANY product FULLY MATCHES provided input (case sensitive) on Internal Reference,
  you will only see product that matches input on Internal Reference

- if no product matches provided input, the system will switch back to the original
  search by name (instead of show no results).

Take note that if you type "a1" you will still see all products listed in the example,
because the search will not find any case sensitive match for A1, so the system will
switch back to the original search, which is case insensitive ;-)

## Configuration

Installing the module will automatically enable this on:

- Most backend Product and Product Template views
- the e-Commerce product search bar
