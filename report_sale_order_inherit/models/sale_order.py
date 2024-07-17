from odoo import models, fields


class SaleOrderReport(models.Model):
    _inherit = 'sale.order'
    _auto = False


    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW sale_order_pivot AS (
                SELECT 
                    id,
                    date_order,
                    partner_id,
                    amount_total,
                    state
                FROM
                    sale_order
                WHERE 
                    is_booking = True
            )
        """)
