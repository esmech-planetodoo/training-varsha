from odoo import api,fields,models

class TeacherDetails (models.Model):
    _inherit = 'res.partner'

    isteacher=fields.Boolean(String="Is Teacher")
    salary   =fields.Float(String="Salary")
