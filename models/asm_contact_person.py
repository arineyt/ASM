from odoo import models, fields


class ContactPerson(models.Model):
    """A class used to represent car owner or representative"""
    _name = 'asm.contact.person'
    _inherit = ['asm.person.mixin', ]
    _description = 'Contact person'

    trust_state = fields.Selection([
        ('trusted', 'Trusted'),
        ('blacklisted', 'Blacklisted')
    ], string='Trust Status', default='trusted')

    description = fields.Text()

    def name_get(self):
        return [(rec.id,
                 "%s %s %s" % (rec.last_name, rec.middle_name, rec.first_name)
                 ) for rec in self]
