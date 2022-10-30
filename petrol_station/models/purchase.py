# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    driver_id = fields.Many2one('res.partner',string="Driver")