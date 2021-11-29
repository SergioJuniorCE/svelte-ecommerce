'use strict';
const { sanitizeEntity } = require('strapi-utils');
/**
 * Read the documentation (https://strapi.io/documentation/developer-docs/latest/development/backend-customization.html#core-controllers)
 * to customize this controller
 */

 module.exports = {
  /**
   * Retrieve a record.
   * 
   * @return {Object}
   */

  async findOne(ctx) {
    const { slug } = ctx.params;
    const product = await strapi.services.category.findOne({ slug });
    return sanitizeEntity(product, { model: strapi.models.product });
  }
}