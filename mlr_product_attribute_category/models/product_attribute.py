# custom_addon/models/product_attribute.py
from odoo import models, fields

class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    category_name = fields.Char(string='Attribute Category')
