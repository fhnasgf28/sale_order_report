from odoo import models


class SaleBookingOrderXlsx(models.Model):
    _name = 'report.report_sale_order_inherit.report_booking_order_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Report Sale Order Booking Report'

    def action_generate_reportXlsx(self, workbook, data, orders):
        sheet = workbook.add_worksheet('Sale Booking Order Report')

        #header
        header_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
        sheet.set_row(0, 30, header_format)
        sheet.write(0, 0, 'Order ID', header_format)
        sheet.write(0, 1, 'Order Date', header_format)
        sheet.write(0, 2, 'Customer', header_format)
        sheet.write(0, 3, 'Total Amount', header_format)
        sheet.write(0, 4, 'Status', header_format)
        sheet.write(0, 5, 'Product', header_format)
        sheet.write(0, 6, 'Description', header_format)
        sheet.write(0, 7, 'Quantity', header_format)
        sheet.write(0, 8, 'Quantity Booking', header_format)
        sheet.write(0, 9, 'Unit Price', header_format)
        sheet.write(0, 10, 'Taxes', header_format)
        sheet.write(0, 11, 'Subtotal', header_format)
        sheet.write(0, 12, 'Payment Terms', header_format)

        # Data
        row = 1
        for order in orders:
            for line in order.order_line:
                col = 0
                sheet.write(row, col, order.name)
                sheet.write(row, col + 1, order.date_order.strftime('%Y-%m-%d') if order.date_order else '')
                sheet.write(row, col + 2, order.partner_id.name)
                sheet.write(row, col + 3, order.amount_total)
                sheet.write(row, col + 4, order.state)
                sheet.write(row, col + 5, line.product_id)
                sheet.write(row, col + 6, line.product_id.name)
                sheet.write(row, col + 7, line.product_uom_qty)
                sheet.write(row, col + 8, line.qty_booking)
                sheet.write(row, col + 9, line.price_unit)
                sheet.write(row, col + 9, line.tax_id.name)
                sheet.write(row, col + 9, line.price_subtotal)

                row += 1

        sheet.set_column(0, 0, 30)
