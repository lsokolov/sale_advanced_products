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

from openerp.osv import fields, osv
# from openerp.tools.translate import _


class adv_product_order_wizard(osv.Transientmodel):
    _name = 'adv.product.order.wizard'

    
    _columns = {
        'in': fields.boolean('Internal form'),
        'out': fields.boolean('Form for client'),
    }
    
    _defaults = {
        'in': 1,
        'out': 1,
    }
    
    def order_print(self, cr, uid, ids, context=None):
        """
        To get the date and print the report
        @return : return report
        """
        if context is None:
            context = {}
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, ['in','out'], context=context)
        res = res and res[0] or {}
        res['price_list'] = res['price_list'][0]
        datas['form'] = res
        if res['prn_img'] is True:
            report = 'product.pricelist.extra'
        else:
            report = 'product.pricelist'
        
        return {
            'type': 'ir.actions.report.xml',
            'report_name': report,
            'datas': datas,
       }

# adv_products_order_print()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

