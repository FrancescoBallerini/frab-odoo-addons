<h2>Product Form Pricelist: Percent Change</h2>

Module Features
---------------

- Full access to product pricelist rule form-view by product form-view.


-  A computed field 'Selling Price' shows the selling price for active product template or variant depending on provided parameters


- <b>Percent change</b>: click button <b>"Set Price Discount %"</b>
    to compute the percent change based on <b>Selling Price</b> (recomputed on button click) and a <b>User
    Input</b> which will represent the new selling price. Percent change formula:


     (user input - selling price computed) / selling price computed x 100
 

  The result will be stored in <b>Price Discount</b> field or <b>Percent Price</b>
  depending on "Compute Price" parameter.

  Rule based on other pricelist outcome are supported:

![alt text](./static/description/demo_based_on_pricelist.png)

<b>Selling Price Computation:</b> In this example we set a rule for a Storage Box that cost &euro;5.
            We apply a rule based on another pricelist outcome, which applies a markup of 200%. When we set
            the pricelist dependency the +200% outcome will be applied, so the field "Selling Price" will be computed
            to &euro;15. Then we set an additional 5% increment on the outcome for this product rule, so the price will
            now be recomputed at &euro;15.75.

![alt text](./static/description/demo_set_percent_price_variant.png)

<b>Percent Change Computation:</b> we want to set the percentage Price Discount after we apply the +200% pricelist
            on a product variant that we want to sell for &euro;19. We select Compute price "Formula" and "Based On
            Other Pricelist" and select the Office Furniture: +200% Pricelist. The pricelist outcome is applied on the
            product category which correspond to the product variant category, so the Selling Price will be computed to
            &euro;15. We now provide an input to compute the Price Discount that we need to apply in order to sell the 
            product at &euro;19, and click on "Set Price Discount". Price Discount will be computed and stored to -26.67%.
            
            

Other info
---------------
* This module extends [product_form_pricelist](https://github.com/OCA/product-attribute/tree/14.0/product_form_pricelist) from
  [OCA Product Attribute Repository](https://github.com/OCA/product-attribute/tree/14.0), so you will need it in your Odoo instance to be able to install this module.


*  <b>Product Variants:</b> product variant workflow has been taken into consideration in the developement process when it was possible so this module should provide
   a decent base for compatibility with product variant workflow. Despite that, depending on what you need to do it might require some extra implementation to be
   effective.


* If you install [Product Proicelist SupplierInfo](https://github.com/OCA/product-attribute/tree/14.0/product_pricelist_supplierinfo) and configure a
  "Based On - Prices based on supplier info" rule, selling price for retrieved vendor will be computed but it's not a full impelemntation.
  Might be improved in future but there is no plan for it at  the moment.
                
  
Technical info
---------------

* <b>Performance:</b> this module makes use of computed field which are not stored by default. This allows smooth installation process
    and avoid to use database space, but leave computed fields as non-stored might be impacting a lot on performance, expecially if you
    have a lot of pricelist rules for specific products. If you plan to use or try this module you should consider to set store=True on 
    all computed fields that are set by _compute_product_pricelist_selling_price() function.

Contacts
---------------

If you have any queries or doubt you can contact me on:

* email: francescobl.lavoro@gmail.com

* discord: Francesco Ballerini#6462
