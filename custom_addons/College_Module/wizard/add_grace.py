from odoo import fields, models, api, _

class AddGrace(models.TransientModel):
     _name = 'add.grace'

     addmarks = fields.Integer(String="Add Grace Marks")

     def update_marks(self):
         active_ids = self._context.get('active_ids') or self._context.get('active_id')
         id = self.env['subject.details'].search([('id', '=', active_ids)])

         for rec in id:
             if rec:
                 rec.total = rec.total + self.addmarks
                 rec.percentage= (rec.total/4)

     def cancel(self):
         """To close wizard"""
         return {'type': 'ir.actions.act_window_close'}