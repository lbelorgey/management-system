# Copyright 2020 Laurent Bélorgey
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MgmtsystemHazard(models.Model):
    _inherit = 'mgmtsystem.hazard'

    prevention_measure_ids = fields.Many2many(
        'document.page',
        'mgmtsystem_hazard_prevention_measure_rel',
        'hazard_id',
        'prevention_measure_id',
        'Prevention Measures',
    )
