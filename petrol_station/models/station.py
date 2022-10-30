# -*- coding: utf-8 -*-

from odoo import models, fields, api


class petrolStation(models.Model):
    _name = 'petrol.station'
    _description = 'Petrol Station'

    name = fields.Char(string="Name")
    shift_ids = fields.One2many('station.shifts','petrol_station_id',string="Shifts")
    pump_ids = fields.One2many('pump.pump','station_id',string="Pumps")