from odoo import api,fields,models

class LibraryDetails(models.Model):
    _name = 'library.details'

    book_id  = fields.One2many('book.details','library_id', string='Book Reference')
    bookname    = fields.Char(String="Book Name")
    issue_date  = fields.Date(String="Issued Date")
    return_date = fields.Date(String="Return Date")

