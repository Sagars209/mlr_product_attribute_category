# custom_addon/models/product_attribute.py
from odoo import models, fields

class ProductTemplateAttributeLine(models.Model):
    _inherit = 'product.template.attribute.line'

    category_name = fields.Char(related='attribute_id.category_name', string="Attribute Category")
