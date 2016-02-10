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

import logging
from openerp.osv import fields
from openerp.osv import osv
import datetime
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class sale_advanced_products(osv.osv):
    _name = 'sale.advanced.products'

    def _set_order_name(self, cr, uid, ids, context=None):
        try:
            res = 'AO/' + str(max(self.search(cr, uid, [], order='id')) + 1).zfill(4)
        except:
            res = 'AO/0001'

        return res

    _columns = {
        'name': fields.char('Order name', required=True, readonly=True),
        'link': fields.char('Link'),
        'description': fields.text('Description'),
        'state': fields.selection([
            ('draft', 'Draft'),
            ('calc', 'Calculated'),
        ], 'Status', readonly=False, select=True),
        'create_date': fields.date('Creation Date', readonly=True, select=True),
        'calc_date': fields.date('Calculation Date', readonly=True, select=True),
        'user_id': fields.many2one('res.users', 'Salesperson', required=True, readonly=False, select=True),
        'partner_id': fields.many2one('res.partner', 'Customer', readonly=False, required=True, change_default=True,
                                      select=True),
        'sale_order_id': fields.many2one('sale.order', 'Sale Order', readonly=True, change_default=True, select=True),
        'complicity': fields.float('Complicity production', readonly=False),
        'attachments': fields.many2many('ir.attachment', 'class_ir_attachments_rel', 'class_id', 'attachment_id',
                                        'Attachments'),

        'body_l': fields.integer('Length', readonly=False),
        'body_w': fields.integer('Width', readonly=False),
        'body_h': fields.integer('Height', readonly=False),
        'body_door': fields.integer('Doors', readonly=False),
        'body_rack': fields.integer('Shelvs', readonly=False),
        'body_side': fields.many2one('product.template', 'Sidewall', domain=[('furn_body', '=', True)], readonly=False),
        'body_front': fields.many2one('product.template', 'Facade', domain=[('furn_body', '=', True)], readonly=False),
        'body_bott': fields.many2one('product.template', 'Bottom', domain=[('furn_body', '=', True)], readonly=False),

        'find_hand1_type': fields.many2one('product.template', 'Handle 1 Type', domain=[('furn_hand', '=', True)],
                                           readonly=False),
        'find_hand1_qty': fields.integer('Handle 1 Qty', readonly=False),
        'find_hand2_type': fields.many2one('product.template', 'Handle 2 Type', domain=[('furn_hand', '=', True)],
                                           readonly=False),
        'find_hand2_qty': fields.integer('Handle 2 Qty', readonly=False),
        'find_loop1_type': fields.many2one('product.template', 'Hinge 1 Type', domain=[('furn_loop', '=', True)],
                                           readonly=False),
        'find_loop1_qty': fields.integer('Loop 1 Qty', readonly=False),
        'find_loop2_type': fields.many2one('product.template', 'Hinge 2 Type', domain=[('furn_loop', '=', True)],
                                           readonly=False),
        'find_loop2_qty': fields.integer('Loop 2 Qty', readonly=False),
        'find_fix_type': fields.many2one('product.template', 'Small ironware Type', domain=[('furn_fix', '=', True)],
                                         readonly=False),
        'find_fix_qty': fields.integer('Small ironware Qty', readonly=False),
        'find_anhand_qty': fields.integer('Anti-handle Qty', readonly=False),

        'furn_box': fields.one2many('sale.advanced.products.box', 'adv_prod_order_id', 'Drawers', readonly=False),

        'furn_aldoors': fields.one2many('sale.advanced.products.aldoors', 'adv_prod_order_id', 'Aluminium doors',
                                        readonly=False),

        'furn_add': fields.one2many('sale.advanced.products.add', 'adv_prod_order_id', 'Additional materials',
                                    readonly=False),

        'acc_light_type': fields.many2one('product.template', 'Type', domain=[('furn_light', '=', True)],
                                          readonly=False),
        'acc_light_l': fields.integer('Lengths', readonly=False),
        'acc_switch': fields.boolean('Sensor switch'),
        'acc_bin_type': fields.many2one('product.template', 'Bucket Type', domain=[('furn_bin', '=', True)],
                                        readonly=False),
        'acc_bin_qty': fields.integer('Bucket Qty', readonly=False),
        'acc_towel_type': fields.many2one('product.template', 'Towel holder Type', domain=[('furn_towel', '=', True)],
                                          readonly=False),
        'acc_towel_qty': fields.integer('Towel holder Qty', readonly=False),
        'acc_cut': fields.boolean('Neckline'),
        'acc_hand_cut_qty': fields.integer('Neckline type handle qty', readonly=False),

        'body_price': fields.float('Corps price', readonly=True),
        'body_price_free': fields.float('Corps price (without K)', readonly=True),
        'find_price': fields.float('Furniture price', readonly=True),
        'find_price_free': fields.float('Furniture price (without K)', readonly=True),
        'add_price': fields.float('Adds price', readonly=True),
        'add_price_free': fields.float('Adds price (without K)', readonly=True),
        'acc_price': fields.float('Accessories price', readonly=True),
        'acc_price_free': fields.float('Accessories price (without K)', readonly=True),
        'work_price': fields.float('Work price', readonly=True),
        'work_price_free': fields.float('Work price (without K)', readonly=True),
        'total_price': fields.float('Total price', readonly=True)
    }

    _defaults = {
        'name': _set_order_name,
        'user_id': lambda self, cr, uid, context: uid,
        'create_date': datetime.datetime.now().date(),
        'find_fix_qty': 2,
        'complicity': 1
    }

    def unlink(self, cr, uid, ids, context=None):
        unlink_ids = []
        for order in self.browse(cr, uid, ids, context=context):
            # Check sale order
            if order.sale_order_id:
                raise osv.except_osv(_('Invalid Action!'), _(
                    'To delete advanced order, you must delete sale order ' + order.sale_order_id.name + ' before!'))
            else:
                unlink_ids.append(order.id)
                # Unlink boxes and adds
                if order.furn_box:
                    for box in order.furn_box:
                        box.unlink()
                if order.furn_add:
                    for add in order.furn_add:
                        add.unlink()
                if order.attachments:
                    for attach in order.attachments:
                        attach.unlink()

        return osv.osv.unlink(self, cr, uid, unlink_ids, context=context)

    def adv_order_calc(self, cr, uid, ids, context=None):

        for order in self.browse(cr, uid, ids, context):

            coef_list = {}
            for n in range(1, 6):
                coef_list['c' + str(n)] = float('1.0')

            # Calculating coefficients
            for n in range(1, 6):
                coef = float(self.pool.get('ir.config_parameter').get_param(cr, uid, 'furn_coef' + str(n)))
                if coef:
                    coef_list['c' + str(n)] = coef

            # Calculate body price
            price_body_side = (order.body_w * order.body_h * 2 * order.body_side.list_price) / 1000000
            price_body_front = (order.body_l * order.body_h * order.body_front.list_price) / 1000000
            price_body_bott = (order.body_l * order.body_w * order.body_bott.list_price) / 1000000
            if price_body_side and price_body_front and price_body_bott:
                price_minifix = self.read_price(cr, uid, 'furn_minifix')
                price_shkanta = self.read_price(cr, uid, 'furn_shkanta')
            else:
                price_minifix = 0
                price_shkanta = 0

            price_body = (price_body_side + price_body_front + price_body_bott) + 32 * price_minifix + 64 * price_shkanta

            # Calculate find price
            price_hand = order.find_hand1_type.list_price * order.find_hand1_qty + order.find_hand2_type.list_price * order.find_hand2_qty
            price_loop = order.find_loop1_type.list_price * order.find_loop1_qty + order.find_loop2_type.list_price * order.find_loop2_qty
            price_fix = order.find_fix_type.list_price * order.find_fix_qty
            price_anhand = order.body_l * order.find_anhand_qty * (
                self.read_price(cr, uid, 'furn_anhand') + 2 * self.read_price(cr, uid, 'furn_anhand_fix')) / 1000

            # Calculate box price
            price_box_mat = self.read_price(cr, uid, 'furn_box_mat')
            price_box = 0
            price_box_w = 0
            for box in order.furn_box:
                price_box += ((
                              box.box_w * box.box_l + box.box_w * 100) * price_box_mat / 1000000 + box.way.list_price) * box.box_qty
                price_box_w = price_box_w + box.box_w * box.box_qty

            # Calculate aldoors price
            price_aldoors = 0
            doors_qty = 0
            for door in order.furn_aldoors:
                price_aldoors += (float(self.read_price(cr, uid, 'furn_door_angle')) * (door.aldoor_l + door.aldoor_w) / 1000
                    + (float(self.read_price(cr, uid, 'furn_door_prof'))
                    + door.aldoor_l * door.aldoor_w * float(self.read_price(cr, uid, 'furn_door_glass')) / 1000000))*door.aldoor_qty
                doors_qty = doors_qty + door.aldoor_qty
            price_find = price_hand + price_loop + price_fix + price_anhand + price_box + price_aldoors

            # Calculate add price
            price_add = 0
            price_add_work = 0
            for add in order.furn_add:
                price_add += (add.type.list_price * add.length * add.width * add.qty) / 1000000
                if add.templ:
                    add_w = 1.1
                else:
                    add_w = 1
                price_add_work += add.length * 0.06 * add.qty * add_w

            # Calculate acc price
            price_light = order.acc_light_type.list_price * order.acc_light_l
            if order.acc_switch:
                price_switch = float(self.read_price(cr, uid, 'furn_switch'))
            else:
                price_switch = 0
            price_bin = order.acc_bin_type.list_price * order.acc_bin_qty
            price_towel = order.acc_towel_type.list_price * order.acc_towel_qty
            if order.acc_cut:
                price_cut = float(self.read_price(cr, uid, 'furn_cut'))
            else:
                price_cut = 0
            price_hand_cut = float(self.read_price(cr, uid, 'furn_hand_cut')) * order.acc_hand_cut_qty

            price_acc = price_light + price_switch + price_bin + price_towel + price_cut + price_hand_cut

            # Calculate work price
            price_z = float(self.read_price(cr, uid, 'furn_boxing')) + float(self.read_price(cr, uid, 'furn_drilling'))
            price_rk = 0.04 * order.body_l + 4 + order.body_h * 0.01
            if doors_qty == 0:
                doors_qty = order.body_door
            price_rf = 60 + 0.03 * price_box_w + (10 + order.body_h * 0.02) * doors_qty + (
                                                                                              order.find_hand1_qty + order.find_hand2_qty) * 2 + order.find_anhand_qty * 6 + price_add_work
            if order.acc_light_type:
                price_light_w = self.read_price(cr, uid, 'furn_acc_light_w')
            else:
                price_light_w = 0
            if order.acc_switch:
                price_switch_w = self.read_price(cr, uid, 'furn_acc_switch_w')
            else:
                price_switch_w = 0
            if order.acc_bin_type:
                price_bin_w = self.read_price(cr, uid, 'furn_acc_bin_w')
            else:
                price_bin_w = 0
            if order.acc_towel_type:
                price_towel_w = self.read_price(cr, uid, 'furn_acc_towel_w')
            else:
                price_towel_w = 0

            price_ra = price_light_w + price_switch_w + price_bin_w + price_towel_w

            price_work = price_z + price_rk + price_rf + price_ra

            # Calculate order price
            price = price_body * coef_list['c1'] + price_find * coef_list['c2'] + price_add * coef_list[
                'c3'] + price_acc * coef_list['c4'] + price_work * coef_list['c5']

            self.write(cr, uid, order.id, {'body_price': price_body * coef_list['c1']})
            self.write(cr, uid, order.id, {'body_price_free': price_body})
            self.write(cr, uid, order.id, {'find_price': price_find * coef_list['c2']})
            self.write(cr, uid, order.id, {'find_price_free': price_find})
            self.write(cr, uid, order.id, {'add_price': price_add * coef_list['c3']})
            self.write(cr, uid, order.id, {'add_price_free': price_add})
            self.write(cr, uid, order.id, {'acc_price': price_acc * coef_list['c4']})
            self.write(cr, uid, order.id, {'acc_price_free': price_acc})
            self.write(cr, uid, order.id, {'work_price': price_work * coef_list['c5']})
            self.write(cr, uid, order.id, {'work_price_free': price_work})
            self.write(cr, uid, order.id, {'total_price': price * order.complicity})
            self.write(cr, uid, order.id, {'calc_date': datetime.datetime.now().date()})
        return True

    def read_price(self, cr, uid, field):
        products = self.pool.get('product.template')
        prod_id = int(self.pool.get('ir.config_parameter').get_param(cr, uid, field))
        try:
            price = products.read(cr, uid, prod_id, ['list_price'])['list_price']
            return price
        except:
            return 0


class product_template(osv.osv):
    _name = 'product.template'
    _inherit = 'product.template'
    _columns = {
        'furn_body': fields.boolean('Corps'),
        'furn_hand': fields.boolean('Handle'),
        'furn_loop': fields.boolean('Hinge'),
        'furn_fix': fields.boolean('Fastener'),
        'furn_way': fields.boolean('Slide'),
        'furn_add': fields.boolean('Add. mat.'),
        'furn_light': fields.boolean('Backlight'),
        'furn_bin': fields.boolean('Bucket'),
        'furn_towel': fields.boolean('Towel holder')
    }

    _defaults = {
        'furn_body': False,
        'furn_hand': False,
        'furn_loop': False,
        'furn_fix': False,
        'furn_way': False,
        'furn_add': False,
        'furn_light': False,
        'furn_bin': False,
        'furn_towel': False
    }


class sale_advanced_products_box(osv.osv):
    _name = 'sale.advanced.products.box'
    _columns = {
        'box_l': fields.integer('Length', readonly=False),
        'box_w': fields.integer('Width', readonly=False),
        'box_qty': fields.integer('Qty', readonly=False),
        'way': fields.many2one('product.template', 'Slides', domain=[('furn_way', '=', True)], readonly=False),
        'adv_prod_order_id': fields.many2one('sale.advanced.products', 'Advanced Product Order'),
    }

    _defaults = {
        'box_qty': 1,
    }


class sale_advanced_products_aldoors(osv.osv):
    _name = 'sale.advanced.products.aldoors'
    _columns = {
        'aldoor_l': fields.integer('Length', readonly=False),
        'aldoor_w': fields.integer('Width', readonly=False),
        'aldoor_qty': fields.integer('Qty', readonly=False),
        'adv_prod_order_id': fields.many2one('sale.advanced.products', 'Advanced Product Order'),
    }

    _defaults = {
        'aldoor_qty': 1,
    }


class sale_advanced_products_add(osv.osv):
    _name = 'sale.advanced.products.add'
    _columns = {
        'length': fields.integer('Length', readonly=False),
        'width': fields.integer('Width', readonly=False),
        'qty': fields.integer('Qty', readonly=False),
        'templ': fields.boolean('Template'),
        'type': fields.many2one('product.template', 'Type', domain=[('furn_add', '=', True)], readonly=False),
        'adv_prod_order_id': fields.many2one('sale.advanced.products', 'Advanced Product Order'),
    }


class sale_advanced_products_settings(osv.TransientModel):
    _name = 'sale.advanced.products.settings'
    _inherit = 'res.config.settings'
    _columns = {
        'furn_box_mat': fields.many2one('product.template', 'Drawers material'),
        'furn_anhand': fields.many2one('product.template', 'Anti-handle'),
        'furn_anhand_fix': fields.many2one('product.template', 'Anti-handle fastener'),
        'furn_minifix': fields.many2one('product.template', 'Minifix'),
        'furn_shkanta': fields.many2one('product.template', 'Shkanta'),
        'furn_switch': fields.many2one('product.template', 'Sensory switch'),
        'furn_cut': fields.many2one('product.template', 'Neckline'),
        'furn_hand_cut': fields.many2one('product.template', 'Neckline type handle'),
        'furn_door_angle': fields.many2one('product.template', 'Al doors angle'),
        'furn_door_prof': fields.many2one('product.template', 'Al doors profile'),
        'furn_door_glass': fields.many2one('product.template', 'Al doors glass'),
        'furn_boxing': fields.many2one('product.template', 'Boxing'),
        'furn_drilling': fields.many2one('product.template', 'Drilling'),
        'furn_acc_light_w': fields.many2one('product.template', 'Backlighting'),
        'furn_acc_switch_w': fields.many2one('product.template', 'Switch'),
        'furn_acc_bin_w': fields.many2one('product.template', 'Bucket'),
        'furn_acc_towel_w': fields.many2one('product.template', 'Towel holder'),
        'furn_coef1': fields.float('Corps coefficient'),
        'furn_coef2': fields.float('Furniture coefficient'),
        'furn_coef3': fields.float('Adds coefficient'),
        'furn_coef4': fields.float('Accessories coefficient'),
        'furn_coef5': fields.float('Works coefficient'),

    }

    def get_default_furn(self, cr, uid, fields, context=None):
        def_val = {}
        for fil in fields:
            def_val[fil] = float(self.pool.get('ir.config_parameter').get_param(cr, uid, fil))
        return def_val

    def set_furn(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids)
        parameters = self.pool.get('ir.config_parameter')
        for conf in config:
            fields = conf.fields_get()
            for fil in fields:
                if fields[fil]['type'] == 'many2one':
                    exec 'val = conf.' + fil + '.id'
                    if 'furn' in fil:
                        if val:
                            parameters.set_param(cr, uid, fil, val)
                        else:
                            param_id = parameters.search(cr, uid, [('key', '=', fil)])
                            parameters.browse(cr, uid, param_id).unlink()

                else:
                    val = self.read(cr, uid, conf.id, [fil])[fil]
                    if 'furn' in fil and val:
                        parameters.set_param(cr, uid, fil, val)
        return True
