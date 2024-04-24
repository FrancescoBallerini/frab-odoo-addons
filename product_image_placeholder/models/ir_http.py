from odoo import models

PRODUCT_MODELS = ["product.template", "product.product"]

PRODUCT_IMAGE_FIELDS = [
    "image_1920",
    "image_1024",
    "image_512",
    "image_128",
    "image_128",
]


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def binary_content(
        self,
        xmlid=None,
        model="ir.attachment",
        id=None,
        field="datas",
        unique=False,
        filename=None,
        filename_field="name",
        download=False,
        mimetype=None,
        default_mimetype="application/octet-stream",
        access_token=None,
    ):
        if model in PRODUCT_MODELS and field in PRODUCT_IMAGE_FIELDS:
            obj = None
            if xmlid:
                obj = self._xmlid_to_obj(self.env, xmlid)
            elif id and model in self.env:
                obj = self.env[model].browse(int(id))
            if obj and not obj[field]:
                # `obj[field]` is the current requested image field for the product:
                # when image field hasn't content a placeholder is loaded. You can
                # find default placeholder in `/web/static/src/img/placeholder.png`
                # Even if the standard placeholder is actually an image its content
                # will be evaluated as `false` in python thus we can check if a
                # different image has been loaded and if not, we replace the content
                # with the product placeholder
                product_placeholder = self.env["product.image.placeholder"].search(
                    [], order="sequence asc", limit=1
                )
                if product_placeholder and product_placeholder.image_placeholder:
                    return super(IrHttp, self).binary_content(
                        xmlid=xmlid,
                        model=product_placeholder._name,
                        id=product_placeholder.id,
                        field="image_placeholder",
                        unique=unique,
                        filename=filename,
                        filename_field=filename_field,
                        download=download,
                        mimetype=mimetype,
                        default_mimetype=default_mimetype,
                        access_token=access_token,
                    )
        return super(IrHttp, self).binary_content(
            xmlid=xmlid,
            model=model,
            id=id,
            field=field,
            unique=unique,
            filename=filename,
            filename_field=filename_field,
            download=download,
            mimetype=mimetype,
            default_mimetype=default_mimetype,
            access_token=access_token,
        )
