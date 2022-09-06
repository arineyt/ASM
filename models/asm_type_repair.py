from odoo import fields, models


class TypeOfRepair(models.Model):
    """A class used to represent a possible types of repair"""
    _name = 'asm.type.repair'
    _description = 'Type repair'

    name = fields.Char(required=True)
