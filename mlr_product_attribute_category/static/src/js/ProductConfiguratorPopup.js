odoo.define('mlr_product_attribute_category.ProductConfiguratorPopup', [
    '@point_of_sale/app/store/product_configurator_popup/product_configurator_popup', 
    '@web/core/utils/patch',
],  function (require) {
    'use strict';

    const { ProductConfiguratorPopup } = require('@point_of_sale/app/store/product_configurator_popup/product_configurator_popup');
    const { patch } = require('@web/core/utils/patch');

    patch(ProductConfiguratorPopup.prototype,  {	

		setup() {
			super.setup();

			const uniqueCategoriesSet = new Set();
			const attributeList = {};
			this.props.attributes.forEach(attribute => {
				uniqueCategoriesSet.add(attribute.category_name);
				attributeList[attribute.name]=attribute.category_name;
			});
			const uniqueCategoriesArray = Array.from(uniqueCategoriesSet);

			this.state.attributes= uniqueCategoriesArray;
			this.state.attributeList= attributeList;
		},
			// Extend or override methods here
		showAndHideField(event) {
			const elements = document.querySelectorAll('div.attribute.mb-4');

			elements.forEach(element => {
				console.log(element); // Perform any action on the elements
			});

			elements.forEach(element => {
				// Find the span inside the div with class 'attribute_name'
				const spanElement = element.querySelector('div.attribute_name span');
		
				// Check if the span text is 'ATTR1'
				if ((spanElement && this.state.attributeList[spanElement.textContent.trim()] === this.state.category) || this.state.category === 'all') {
					// Hide the entire element
					element.style.display = '';
				}
				else
					element.style.display='none';
			});
			// you can show the element by removing class
		}
    });
});
