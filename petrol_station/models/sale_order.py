# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"


    petrol_station_id = fields.Many2one('petrol.station',string="Staion")
    shift_id = fields.Many2one('station.shifts',string="Shift")
    station_order = fields.Boolean(string="Station Order")
    pump_ids = fields.Many2many('pump.pump',string="Pumps",compute='_compute_pump_ids')
    product_ids = fields.Many2many('product.product',string="Products",compute='_compute_product_ids')

    @api.depends('petrol_station_id')
    def _compute_pump_ids(self):
        for rec in self:
            rec.pump_ids = rec.petrol_station_id.pump_ids.ids

    
    @api.depends('station_order')
    def _compute_product_ids(self):
        for order in self:
            if order.station_order == True:
                product_ids = self.env['product.product'].search([('is_station_product','=',True)])
            else:
                product_ids = self.env['product.product'].search([('is_station_product','!=',True)])

            order.product_ids = product_ids.ids


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    pump_id = fields.Many2one('pump.pump',string="Gas Pump")
    initial_odometer_reading = fields.Float(string="Initial Odometer Reading")
    last_odometer_reading = fields.Float(string="Last Odometer Reading")
    petrol_station_id = fields.Many2one('petrol.station',related='order_id.petrol_station_id',string="Staion")
    
    

    @api.onchange('initial_odometer_reading','last_odometer_reading')
    def onchange_odometer_readings(self):
        if self.last_odometer_reading > 0 and self.initial_odometer_reading > 0:
            self.product_uom_qty = self.initial_odometer_reading - self.last_odometer_reading 

    
    @api.onchange('product_id','pump_id')
    def onchange_pro_pump(self):
        sale_order_line = self.env['sale.order.line'].search([
            ('order_id.state', 'not in', ('draft', 'sent', 'cancel')),
            ('product_id', '=', self.product_id.id),
            ('pump_id', '=', self.pump_id.id),
            ('petrol_station_id','=',self.order_id.petrol_station_id.id)], order='id desc', limit=1)


        if sale_order_line:
            self.last_odometer_reading = sale_order_line.last_odometer_reading