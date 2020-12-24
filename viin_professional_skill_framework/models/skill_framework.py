from odoo import fields,models,api

class ProfessionalSkillFramework(models.Model):
    _name='skill.framework'
    _description='Professional Skill Framework'
    
    name=fields.Char(string='Skill Name', required=True, help='Name of skill')
    code=fields.Char(string='Code', required=True, help='Code of skill')
    description=fields.Char(string='Skill description', required=True, help='Overall description')
 