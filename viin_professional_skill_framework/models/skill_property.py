from odoo import fields, models, api

class GenericProperty(models.Model):
    _name='skill.property' 
    _description='Five generic properties'
    
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
    autonomy=fields.Text(string='Autonomy', required=True)
    influence=fields.Text(string='Influence', required=True)
    complexity=fields.Text(string='Complexity', required=True)
    knowledge=fields.Text(string='Knowledge', required=True)
    business_skill=fields.Text(string='Business skills', required=True)

