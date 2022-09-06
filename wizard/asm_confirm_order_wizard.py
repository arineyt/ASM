from odoo import fields, models


class ConfirmOrderTrust(models.TransientModel):
    _name = 'order.trust.wizard'

    order_id = fields.Many2one('asm.order')
    partner_id = fields.Many2one('asm.contact.person',
                                 string='Customer',
                                 related='order_id.client_id')

    def approve_blacklisted_customer_order(self):
        # call the action_confirm method on the current order
        # include a context to prevent an infinite loop
        self.order_id.with_context({'approve_blacklisted_customer': 1}).write()
