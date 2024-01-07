# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ObservationForm (models.Model):
    _name = "observation.form"
    _inherit = "mail.thread"
    _description = "Demo for observation form"

    name = fields.Char(string='Name', required=True, tracking=True, readonly=True)
    state = fields.Selection([('cancel', 'Rejected'), ('draft', 'Draft'), ('verify', 'Pending'),
                              ('approve', 'Approved'), ], string='Status'
                             , index=True, readonly=True, copy=False, default='draft',
                             help="""* When the request is created the status is \'Draft\'
                            \n* If the request is under verification, the status is \'Waiting\'.
                            \n* If the request is approved then status is set to \'Approved\'.
                            \n* When the admin cancel request the status is \'Rejected\'.""", tracking=True)
    description = fields.Text(string="Description", required=True,
                              readonly=True, states={'draft': [('readonly', False)]})
    date_time = fields.Datetime(string="Date & Time", required=True, readonly=True,
                                 tracking=True)
    location = fields.Selection([('Workshop', 'Workshop'), ('Spot 1', 'Spot 1'), ('Spot 2', 'Spot 2'),
                                ('Spot 3', 'Spot 3'), ], string="Location", readonly=True,
                                 required=True, tracking=True)
    observer_name = fields.Many2one('hr.employee', string="Observer Name", readonly=True,
                                     required=True, tracking=True)
    employee_name = fields.Many2one('hr.employee', string="Employee Name", readonly=True,
                                     required=True, tracking=True)
    observation_team = fields.Boolean(string="Observation Team", default=False)
    team_member_1 = fields.Many2one('hr.employee', string="First Team Member", readonly=True,
                                     tracking=True)
    team_member_2 = fields.Many2one('hr.employee', string="Second Team Member", readonly=True,
                                     tracking=True)
    team_member_3 = fields.Many2one('hr.employee', string="Third Team Member", readonly=True,
                                     tracking=True)
    question_1 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Is there an SOP/SWP for this task ?",
                                  readonly=True,  required=True, tracking=True)
    question_2 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                  string="Has a risk assessment been done for the task ? (Take 5, JSA etc.)",
                                  readonly=True,  required=True, tracking=True)
    question_3 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                  string="Have all people carrying out the task, signed the JSA ?",
                                  readonly=True,  required=True, tracking=True)
    question_4 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                  string="Have all permits required for the"
                                         " task been identified and issued. If “YES list them.",
                                  readonly=True,  required=True, tracking=True)
    question_5 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Have the permits been filled out correctly ?",
                                  readonly=True,  required=True, tracking=True)
    question_6 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Have you identified all hazards of the task ?",
                                  readonly=True,  required=True, tracking=True)
    question_7 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                  string="Have all sources of energy been eliminated or isolated"
                                         " in accordance with SGM equipment isolation policy ? If “YES list them.",
                                  readonly=True,  required=True, tracking=True)
    question_8 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                  string="Are there any dangerous chemicals associated"
                                         " with this task ? If “Yes” list them.",
                                  readonly=True,  required=True, tracking=True)
    question_9 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                  string="Is the worker carrying out this task aware of the associated"
                                         " chemicals and the danger they present ?",
                                  readonly=True,  required=True, tracking=True)
    question_10 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                   string="Is the working environment safe to complete the task ? (bund walls in place"
                                          "\n, weather conditions, hard or soft barricade in place, traffic management"
                                          "\n applied, use of signage etc.). If “YES” describe.",
                                   readonly=True,  required=True, tracking=True)
    question_11 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="What are the control measures on place ?",
                                   readonly=True,  required=True, tracking=True)
    question_12 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Are good housekeeping practices being"
                                                                      " maintained throughout the task ?",
                                   readonly=True,  required=True, tracking=True)
    question_13 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Is the worker wearing the correct "
                                                                      "PPE for the task ?",
                                   readonly=True,  required=True, tracking=True)
    question_14 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Is the PPE being used in good condition ?",
                                   readonly=True,  required=True, tracking=True)
    question_15 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Is the PPE correctly applied ?",
                                   readonly=True,  required=True, tracking=True)
    question_16 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                   string="Does the task require the worker being observed to have mandatory "
                                          "competency-based training?\n i.e machinery operating licenses, trade "
                                          "certificates, working at heights,\n confined space etc. If “YES” list them.",
                                   readonly=True,  required=True, tracking=True)
    question_17 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Has the worker completed this mandatory "
                                                                      "training and is it up to date ?",
                                   readonly=True,  required=True, tracking=True)
    question_18 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Are the correct tools and equipment being "
                                                                      "used for the task? If “NO”, describe.",
                                   readonly=True,  required=True, tracking=True)
    question_19 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Are the tools and equipment in good condition ?"
                                                                      " If “NO”, describe.",
                                   readonly=True,  required=True, tracking=True)
    question_20 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')], string="Are the tools and equipment being used in "
                                                                      "the correct way ? If “NO”, describe.",
                                   readonly=True,  required=True, tracking=True)
    question_21 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                   ('n/a', 'Not Applicable')],
                                   string="Do all electrical tools and equipment being used have a "
                                          "current valid electrical inspection tag attached to the lead ?",
                                   readonly=True,  required=True, tracking=True)
    question_22 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                    ('n/a', 'Not Applicable')],
                                   string="Is the supervisor got involved on hazard identification ?",
                                   readonly=True,  required=True, tracking=True)
    question_23 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                    ('n/a', 'Not Applicable')],
                                   string="Do all electrical tools and equipment being used have a "
                                          "Does the worker clearly understand the task he is carrying out ?",
                                   readonly=True,  required=True, tracking=True)
    question_24 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                    ('n/a', 'Not Applicable')],
                                   string="Is adequate communication being used between workers completing the task?"
                                          " (two-way radios, visual, verbal etc.)",
                                   readonly=True,  required=True, tracking=True)
    question_25 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                    ('n/a', 'Not Applicable')],
                                   string="Are simultaneous operations taking place and have all work "
                                          "parties communicated with each other ?",
                                   readonly=True,  required=True, tracking=True)
    question_26 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                    ('n/a', 'Not Applicable')],
                                   string="Does the worker know what to do in an emergency ?",
                                   readonly=True,  required=True, tracking=True)
    question_27 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                    ('n/a', 'Not Applicable')],
                                   string="Is the worker able to alert the emergency response team ?"
                                          " By what means? (mobile telephone, two-way radio etc.)",
                                   readonly=True,  required=True, tracking=True)
    question_28 = fields.Selection([('c', 'Compliant'), ('un', 'Unacceptable'), ('ni', 'Need Improvement'),
                                    ('n/a', 'Not Applicable')],
                                   string="Does the worker know where the closest fire extinguisher"
                                          " and eye wash station is located ?",
                                   readonly=True,  required=True, tracking=True)
    comment_1 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_2 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_3 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_4 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_5 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_6 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_7 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_8 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_9 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_10 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_11 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_12 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_13 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_14 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_15 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_16 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_17 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_18 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_19 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_20 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_21 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_22 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_23 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_24 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_25 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_26 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_27 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})
    comment_28 = fields.Text(string="Comment", readonly=True, states={'draft': [('readonly', False)]})

    def action_submit_request(self):
        self.write({'state': 'verify'})

    def action_payslip_draft(self):
        return self.write({'state': 'draft'})

    def action_approve(self):
        return self.write({'state': 'approve'})

    def action_refuse(self):
        return self.write({'state': 'cancel'})

    @api.onchange('date_time')
    def onchange_date(self):
        if self.date_time and self.date_time.date() < datetime.now().date():
            raise ValidationError(_("You can't enter a form for a previous date."))

    @api.onchange('date_time', 'location')
    def setting_name(self):
        if self.date_time and self.location:
            self.name = self.location + " - " + str(self.date_time.date())
