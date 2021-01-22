from odoo import api,fields,models
from datetime import date


class BookDetails(models.Model):
    _name = 'book.details'

    library_id = fields.Many2one('library.details', string='Order Reference')
    student_id = fields.Many2one('student.info', string='Order Student')
    name = fields.Char(string="book name")
    author = fields.Char(string="Author")
    price = fields.Char(string="Price")
    description = fields.Char(string="Description")
    isavailable = fields.Boolean(string="Is Available In Library")