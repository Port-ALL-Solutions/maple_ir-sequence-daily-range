# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, timedelta
import logging
import pytz

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IrSequence(models.Model):
    """ Sequence model for daily date range.

    """
    _inherit = 'ir.sequence'
    
    daily_date_range = fields.Boolean(
        string='Daily',
        help='Create daily range instead or yearly',
        default=False
        )

    def _create_date_range_seq(self, date):
        if self.daily_date_range:
                
            today = fields.Date.from_string(date).strftime('%Y-%m-%d')
            date_from = today
            date_to = today
            date_range = self.env['ir.sequence.date_range'].search([('sequence_id', '=', self.id), ('date_from', '>=', date), ('date_from', '<=', date_to)], order='date_from desc')
            if date_range:
                date_to = datetime.strptime(date_range.date_from, '%Y-%m-%d') + timedelta(days=-1)
                date_to = date_to.strftime('%Y-%m-%d')
            date_range = self.env['ir.sequence.date_range'].search([('sequence_id', '=', self.id), ('date_to', '>=', date_from), ('date_to', '<=', date)], order='date_to desc')
            if date_range:
                date_from = datetime.strptime(date_range.date_to, '%Y-%m-%d') + timedelta(days=1)
                date_from = date_from.strftime('%Y-%m-%d')
            seq_date_range = self.env['ir.sequence.date_range'].sudo().create({
                'date_from': date_from,
                'date_to': date_to,
                'sequence_id': self.id,
            })

        else:
        
            seq_date_range = super(IrSequence,self)._create_date_range_seq(date)

        return seq_date_range
