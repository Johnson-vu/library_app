{
    'name': 'Open Academy',
    'summary': 'Manage Training',
    'description': """
        Open Academy module for managing training:
            - training course
            - training session
            - attendees registration
            """,
    'author': 'Viindoo',
    'website': 'viindoo.com',
    'category': 'test',
    'version': '1.0',
    'depend': ['base'],
    'currency':'USD',
    'license':'OPL-1',
    'application': True,
    'data': [
        'security/openacademy_security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        #'views/partner.xml',
        ],
    }