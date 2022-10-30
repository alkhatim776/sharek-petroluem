# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_station_product = fields.Boolean(string="Station Product")