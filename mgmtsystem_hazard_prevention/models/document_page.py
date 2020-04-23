# Copyright 2020 Laurent Bélorgey
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DocumentPage(models.Model):
    _inherit = 'document.page'

    hazard_id = fields.Many2one(
        'mgmtsystem.hazard',
        'Hazard',
        required=False,
        index=True,
    )
