from odoo import api,fields,models
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime,date


class Student1(models.Model):
    _name = 'student.info'

    # order_line = fields.One2many('book.details', 'students', string='Order Lines')
    f_name=fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name", required=True)
    full_name=fields.Char(string="Full Name",compute='get_fullname' , store=True)
    dob=fields.Date("Date Of Birth")
    age=fields.Integer(String="Age", compute='calculate_age', store= True)
    gender=fields.Selection([('M','Male'),('F','Female')],String="Gender")
    rollno=fields.Char(String="Roll No",readonly=True,copy=False )
    phone=fields.Char(string="Phone No")
    email=fields.Char(string="Email")
    subject_ids = fields.One2many('subject.details', 'student_id')
    hobies_ids = fields.One2many('student.hobbies', 'student_id', string='hobbies')

    @api.model
    def create(self, vals):
        if vals.get('rollno', 0) == 0:
            vals['rollno'] = self.env['ir.sequence'].next_by_code('SI')
        result = super(Student1, self).create(vals)
        return result

    @api.depends('dob')
    def calculate_age(self):
        for record in self:
            age_vlaue = relativedelta(datetime.now().date(), fields.Datetime.from_string(record.dob)).years
            record.age=age_vlaue

    @api.depends('f_name', 'l_name')
    def get_fullname(self):
        for record in self:
            record.full_name = str(record.f_name) + ' ' + str(record.l_name)



class Hobbies(models.Model):
    _name = 'student.hobbies'
    student_id = fields.Many2one('student.info', 'Student Id')
    reading=fields.Boolean(string="Reading")
    Swimming =fields.Boolean(string="Swimming")
    dancing=fields.Boolean(string="dancing")

class Subjectdetails(models.Model):
    _name = 'subject.details'

    student_id = fields.Many2one('student.info', string='Student Id')
    chemistry=fields.Integer(string="Chemistry")
    physics=fields.Integer(string="Physics")
    maths=fields.Integer(string="Maths")
    english=fields.Integer(string="English")
    total=fields.Integer(string="Total", compute='calculate_total',store=True)
    percentage=fields.Integer(string="Percentage",store=True)
    status=fields.Char(string="Status" ,store=True )



    @api.depends('chemistry','physics','maths','english')
    def calculate_total(self):
        for record in self:
            total1=int(record.chemistry)+int(record.physics)+int(record.maths)+int(record.english)
            record.total=total1
            percentage1 =(total1/400)*100
            record.percentage=percentage1

            if (percentage1 > 40):
                record.status='pass'
            else:
                record.status='fail'







