from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Car(models.Model):
    """A class used to represent a Car"""
    _name = 'asm.car'
    _description = "Car"

    name = fields.Char(index=True, required=True)
    year_of_issue = fields.Date(required=True)
    age = fields.Integer(compute='_compute_age', compute_sudo=True, store=True)
    degree_of_damage = fields.Selection([('1', 'Good'),
                                         ('2', 'Normal'),
                                         ('3', 'Bad')],
                                        default='1', required=True)
    VIN = fields.Char(srting="VIN", size=17, index=True, required=True)
    photo = fields.Image(max_width=512, max_height=512)
    mileage_of_the_machine = fields.Char()
    personal_manager_id = fields.Many2one('asm.employee', required=True)
    contact_person_id = fields.Many2one('asm.contact.person')

    description = fields.Text()

    @api.depends('year_of_issue')
    def _compute_age(self):
        for car in self:
            car.age = \
                relativedelta(fields.Date.today(), car.year_of_issue).years \
                    if car.year_of_issue else 0
