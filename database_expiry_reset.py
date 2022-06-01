from odoo import api, fields, models, _
from datetime import datetime, timedelta


class DatabaseExpiryReset(models.Model):
    _name = 'database.expiry.reset'

    def database_expiry_reset(self):
        current_date_time = datetime.now()
        updated_date_time = current_date_time + timedelta(days=150)
        updated_date_time = updated_date_time.strftime("%Y-%m-%d %H:%M:%S")
        self.env['ir.config_parameter'].sudo().set_param('database.expiration_date', updated_date_time)

