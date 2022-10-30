# -*- coding: utf-8 -*-
# from odoo import http


# class PetrolStation(http.Controller):
#     @http.route('/petrol_station/petrol_station', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/petrol_station/petrol_station/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('petrol_station.listing', {
#             'root': '/petrol_station/petrol_station',
#             'objects': http.request.env['petrol_station.petrol_station'].search([]),
#         })

#     @http.route('/petrol_station/petrol_station/objects/<model("petrol_station.petrol_station"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('petrol_station.object', {
#             'object': obj
#         })
