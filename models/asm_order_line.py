from odoo import fields, models


class OrderLine(models.Model):
    """A class used to represent line of order"""
    _name = 'asm.order.line'
    _description = 'Order Line'

    name = fields.Text(string='Description')
    order_id = fields.Many2one('asm.order',
                               string='Order Reference',
                               required=True,
                               ondelete='cascade',
                               index=True)
    price_unit = fields.Float(string='Price', required=True, default=0.0)
    type_of_repair_id = fields.Many2one('asm.type.repair',
                                        index=True,
                                        required=True)
