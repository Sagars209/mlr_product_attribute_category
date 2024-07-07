# custom_addon/__manifest__.py
{
    'name': 'Custom Attribute Category',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Adds a category field to product attributes',
    'description': """
    This module adds a category field to the product.attribute model and includes it in all relevant views.
    """,
    'depends': ['base', 'product'],
    'data': [
        'views/product_attribute_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'mlr_product_attribute_category/static/src/js/ProductConfiguratorPopup.js',
	    'mlr_product_attribute_category/static/src/xml/product_configurator_popup.xml',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
