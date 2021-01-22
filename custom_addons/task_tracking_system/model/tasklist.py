from odoo import api,fields,models
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime,date


class Task(models.Model):
    _name = 'task.tracking'
    taskcreated = fields.Date("Task Creation Date")
    taskassigndate = fields.Date("Task Assign Date")
    name= fields.Char(string="Task Name")
    desc = fields.Char(string="Task Description")
    complexity = fields.Char(string="Task Complexity")
    priority = fields.Char(string="Task Priority")
    reviewremark = fields.Char(string="Review Remark")
    assignto = fields.Char(string="Assign To")
    assignby = fields.Char(string="Assign Bye")

    needbydate = fields.Date("Need By Date")
    closedate  = fields.Date("Closure Date")
    taskentry_ids = fields.One2many('task.entry', 'task_id', string='taskentry')


    @api.model
    def create(self, vals):
        res = super(Task, self).create(vals)
        if vals:
           created_review = self.env['task.entry'].create({'task_id':res.id,
                                                         'reviewremark': res.desc})

        return res
        # print(">>>>>>>",created_review)

    def write(self, vals):
        res = super(Task, self).write(vals)

        review = vals.get('desc')
        if vals:
            created_review = self.env['task.entry'].create({'task_id': self.id,
                                                'reviewremark': str(review)
                                                           })
            print("vals>>>>>>>>",res)
        return res
class Taskentry(models.Model):
    _name = 'task.entry'
    reviewremark = fields.Char(string="Review Remark")
    reviewdate = fields.Date(string="Next Review Date")
    task_id = fields.Many2one('task.tracking', 'Tracking Id')