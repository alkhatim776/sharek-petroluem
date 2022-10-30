# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pump(models.Model):
    _name = 'pump.pump'
    _description = 'petrol station pump'

    name = fields.Char(string="Name")
    station_id = fields.Many2one("petrol.station",string="Staion")

