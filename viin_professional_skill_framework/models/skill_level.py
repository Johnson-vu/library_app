from odoo import fields, models, api

class ProfesstionalSkillLevel(models.Model):
    _name='skill.level'
    _description='Professional Skill Levels'
    
    LEVEL_TYPE = [
        ('one', '1-Follow'),
        ('two', '2-Assist'),
        ('three', '3-Apply'),
        ('four','4-Enable'),
        ('five', '5-Ensure, Advise'),
        ('six', '6-Initiate, Influence'),
        ('seven', '7-Set Strategy, Inspire, Mobillise')
    ]
    skill_level=fields.Selection(LEVEL_TYPE,string='Level',required=True, default='one',help="Skill Level")

    
   