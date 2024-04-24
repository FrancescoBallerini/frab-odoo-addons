from odoo import api, fields, models


class ProductImagePlaceholder(models.Model):
    _name = "product.image.placeholder"
    _description = "Placeholder Image For Products"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(string="Sequence")
    image_placeholder = fields.Image(
        string="Product Image Placeholder",
    )

    @api.model
    def default_get(self, fields_list):
        """Override method because the sequence will not automatically
        be incremented when creating a new record, so we assign an explicit
        value in order to avoid that the new `product.image.placeholder` is
        used as the new placeholder (placeholder to show will be chosen
        by getting the `product.image.placeholder` with lower sequence)"""
        res = super(ProductImagePlaceholder, self).default_get(fields_list)
        default_sequence_value = 0
        lower_priority_record = self.env["product.image.placeholder"].search(
            [], order="sequence desc", limit=1
        )
        if lower_priority_record:
            default_sequence_value = lower_priority_record.sequence + 1
        res["sequence"] = default_sequence_value
        return res
