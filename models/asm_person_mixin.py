from odoo import _, fields, models


class PersonMixin(models.AbstractModel):
    """A class used to represent person"""
    _name = 'asm.person.mixin'
    _description = 'Person mixin'

    active = fields.Boolean(default=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    middle_name = fields.Char(required=True)
    gender = fields.Selection(
        default='male',
        selection=[('male', _('Male')),
                   ('female', _('Female'))], required=True)
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Image(max_width=512, max_height=512)

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id,
                        "%s %s %s" % (rec.last_name,
                                      rec.first_name,
                                      rec.middle_name)
                        ))
        return res
