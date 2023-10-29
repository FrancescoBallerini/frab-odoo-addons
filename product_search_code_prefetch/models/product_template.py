from odoo import api, models
from odoo.addons.website.models import ir_http
from odoo.http import request
from odoo.osv import expression


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def _search(
        self,
        args,
        offset=0,
        limit=None,
        order=None,
        count=False,
        access_rights_uid=None,
    ):

        """New behaviour: retrieves provided input value and makes prefetch on `default_code`.
        :returns: any product having `default_code` exactly matching with provided value, if any.
        If no product is matching on provided `default_code`, switch to normal search."""

        code_prefetch = self.env.context.get("product_code_prefetch")
        # product_code_prefetch: from here it's not known if "args" is coming from a
        # SearchView filter, SearchView field or else ("args" is just a list of domain
        # and logic operators). The code prefetch has to be isolated to specific
        # "name search" in order not to break the behaviour of other filter/search domains.
        if code_prefetch:
            # we need to retrieve user input for the search. Unfortunately _search()
            # does not provide user input but only a list of domains and logical operators:
            # we filter out the logical operators and possible default filters (e.g. sale_ok..)
            # by filtering out invalid leafs (operators) and only keep leaf where field=name
            user_input = None
            for arg in args:
                if expression.is_leaf(arg) and arg[0] == "name":
                    # The evaluated leaf (a.k.a. "arg" variable) will be something like:
                    # ['name', 'operator', value]
                    # in form of a list or a tuple...
                    user_input = arg[2]  # ...so this should be the user input : )
                    break
            if user_input:
                # prefetch on default_code
                # use 'in' e list([value]) only to avoid warning:
                # :: the domain term '('default_code', '=', [value])' should use the 'in' or 'not in' operator.
                prefetch_domain = [("default_code", "in", list([user_input]))]
                if ir_http.get_request_website():
                    website_domain = request.website.sale_product_domain()
                    _args = expression.AND([website_domain, prefetch_domain])
                else:
                    _args = prefetch_domain
                ids = super(ProductTemplate, self)._search(
                    _args,
                    offset=offset,
                    limit=limit,
                    order=order,
                    count=count,
                    access_rights_uid=access_rights_uid,
                )
                if ids:
                    return ids
        return super(ProductTemplate, self)._search(
            args,
            offset=offset,
            limit=limit,
            order=order,
            count=count,
            access_rights_uid=access_rights_uid,
        )
