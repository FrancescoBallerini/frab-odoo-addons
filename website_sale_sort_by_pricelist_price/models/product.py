from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # dummy fields > these fields names are
    # used to replace the hyperlinks href of
    # SortBy dropdown menu, but the field
    # value is not relevant, only the name is:
    # field name will be readable from **post
    # in shop() and after super() execution it
    # will lead to a new search() with the field
    # name as context-key.

    # When ProductTemplate.search() is executed
    # it will check for these two context-keys
    # and their presence which will determine:

    # - if a python sortby should be done
    # - whether the `reverse=True` key should
    #   be used or not

    sortby_price_asc = fields.Float()
    sortby_price_desc = fields.Float()

    # Dummy fields must be used instead of simple
    # strings because we still want to call super()
    # for the /shop route when those keys are in **post.
    # This means that on the super() call, the original
    # search is actually done by ORM and it requires
    # a stored field, but that search isn't actually
    # sorting so the field value doesn't matter.

    # For the search() implementation look at the
    # Base module.
