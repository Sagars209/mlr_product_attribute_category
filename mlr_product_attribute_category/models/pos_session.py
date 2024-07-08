# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models
from itertools import groupby


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _get_attributes_by_ptal_id(self):
        # performance trick: prefetch fields with search_fetch() and fetch()
        product_attributes = self.env['product.attribute'].search_fetch(
            [('create_variant', '=', 'no_variant')],
            ['name', 'display_type','category_name'],
        )
        product_template_attribute_values = self.env['product.template.attribute.value'].search_fetch(
            [('attribute_id', 'in', product_attributes.ids)],
            ['attribute_id', 'attribute_line_id', 'product_attribute_value_id', 'price_extra'],
        )
        product_template_attribute_values.product_attribute_value_id.fetch(['name', 'is_custom', 'html_color', 'image'])

        key1 = lambda ptav: (ptav.attribute_line_id.id, ptav.attribute_id.id)
        key2 = lambda ptav: (ptav.attribute_line_id.id, ptav.attribute_id)
        res = {}
        for key, group in groupby(sorted(product_template_attribute_values, key=key1), key=key2):
            attribute_line_id, attribute = key
            values = [{**ptav.product_attribute_value_id.read(['name', 'is_custom', 'html_color', 'image'])[0],
                       'price_extra': ptav.price_extra,
                       # id of a value should be from the "product.template.attribute.value" record
                       'id': ptav.id,
                       } for ptav in list(group) if ptav.ptav_active]
            res[attribute_line_id] = {
                'id': attribute_line_id,
                'name': attribute.name,
                'display_type': attribute.display_type,
                'values': values,
                'sequence': attribute.sequence,
                'category_name': attribute.category_name,
            }

        return res