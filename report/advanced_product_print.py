# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# import time
# from openerp.report import report_sxw
# from openerp.osv import osv
# from openerp import api, models


# class adv_prod_order_ext(report_sxw.rml_parse):
#     def __init__(self, cr, uid, name, context):
#         super(adv_prod_order_ext, self).__init__(cr, uid, name, context)
#         self.net_total = 0.0
#         self.localcontext.update({
#             'time': time,
#             'get_total_qty': self._get_total_qty
#         })
#
#     def _get_total_qty(self, lines):
#         tot_qty = 0
#         for line in lines:
#             tot_qty += line.aldoor_qty or 0
#         return tot_qty
#
#
# class report_sale_advanced_products_ext(osv.AbstractModel):
#     _name = 'report.sale_advanced_products.ext_report_templ'
#     _inherit = 'report.abstract_report'
#     _template = 'sale_advanced_products.ext_report_templ'
#     _wrapped_report_class = adv_prod_order_ext
