# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class ProductUomCategory(models.Model):
    """Enforce unique UOM category name"""

    _inherit = 'product.uom.categ'

    _sql_constraints = [('name_uniq', 'unique (name)', """Category name must be unique."""), ]

    @api.multi
    def copy(self, default=None):
        if not default:
            default = {}
        default = default.copy()
        default['name'] = self.name + _(' (copy)')

        return super(ProductUomCategory, self).copy(default=default)


class ProductUom(models.Model):
    """Enforce unique UOM name"""

    _inherit = 'product.uom'

    _sql_constraints = [('name_uniq', 'unique (name)', """UOM Name must be unique."""), ]

    code = fields.Char(
        string='Code',
        help="Short code to be used externally. e.g. for unit Inch, use code IN.")

    @api.multi
    def copy(self, default=None):
        if not default:
            default = {}
        default = default.copy()
        default['name'] = self.name + _(' (copy)')

        return super(ProductUom, self).copy(default=default)
