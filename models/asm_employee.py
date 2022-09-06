from odoo import models, fields


class Employee(models.Model):
    """A class used to represent an Employee"""
    _name = 'asm.employee'
    _inherit = ['asm.person.mixin', ]
    _description = "Employee"

    position = fields.Char(required=True)
    is_intern = fields.Boolean()
    color = fields.Integer()
    intern_ids = fields.One2many(comodel_name='asm.employee',
                                 inverse_name='mentor_id',
                                 string='Interns',
                                 domain=[('is_intern', '=', True)])
    car_ids = fields.One2many(comodel_name='asm.car',
                              inverse_name='personal_manager_id')
    order_ids = fields.One2many(comodel_name='asm.order',
                                inverse_name='personal_manager_id')
    mentor_id = fields.Many2one(comodel_name='asm.employee',
                                string='Mentor',
                                domain=[('is_intern', '=', False)])

    description = fields.Text()

    def name_get(self):
        return [(rec.id,
                 "%s %s %s" % (rec.last_name, rec.middle_name, rec.first_name)
                 ) for rec in self]
