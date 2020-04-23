# Copyright 2020 Laurent Bélorgey
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Hazard Prevention',
    'version': '12.0.1.0.0',
    "category": 'Management System',
    'author': u'Laurent Bélorgey',
    'license': 'AGPL-3',
    'depends': [
        'document_page_work_instruction',
        'mgmtsystem_hazard',
    ],
    'data': [
        'views/mgmtsystem_hazard.xml',
    ],
    'installable': True,
}
