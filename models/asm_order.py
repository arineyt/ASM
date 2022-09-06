from odoo import fields, models, api, _


class Order(models.Model):
    """A class used to represent an Order"""
    _name = 'asm.order'
    _description = 'Order'

    name = fields.Char(string='Number',
                       required=True,
                       copy=False,
                       readonly=True,
                       index=True,
                       default=lambda self: _('New'))
    client_id = fields.Many2one('asm.contact.person', required=True)
    personal_manager_id = fields.Many2one('asm.employee', required=True)
    car_id = fields.Many2one('asm.car', required=True)
    telephone = fields.Char(related='client_id.phone')
    status = fields.Selection([('accepted', 'Accepted'),
                               ('completed', 'Completed'),
                               ('canceled', 'Canceled')],
                              default='accepted', required=True)
    type_repair_ids = fields.One2many(
        comodel_name='asm.order.line',
        inverse_name='order_id')

    description = fields.Text()

    @api.model
    def create(self, vals):
        # overriding the create method to add the sequence
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('asm.order') or _('New')
        result = super(Order, self).create(vals)
        return result

    def write(self, vals):
        # If partner is not blacklisted, call super,
        # it means that the sale order can be confirmed

        # if there is a context approve_blacklisted_customer
        # it means that this method
        # is called from the order.trust.wizard transient
        # model and the user have
        # 'Approve order of blacklisted customer' access rights,
        # so the sale order can be confirmed
        if self.client_id.trust_state == 'trusted' \
                or 'approve_blacklisted_customer' in self._context:
            super(Order, self).write(vals)
        else:
            # partners is blacklisted
            # create transient model record with the
            # value of order_id is the current sale order id
            # by inserting the order_id field, later in the
            # order.trust.wizard transient model
            # we can call the action_confirm method to confirm this sales order
            wizard_id = self.env['order.trust.wizard'].create({'order_id': self.id})
            return {
                'name': _('Blacklisted Customer'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'order.trust.wizard',
                'res_id': wizard_id.id,
                'target': 'new',
            }
