from odoo import models, fields, api, _
import io
import xlsxwriter
import base64


class BookingOrderReportWizard(models.TransientModel):
    _name = 'booking.order.report.wizard'
    _description = 'Booking Report Wizard xlsx'

    from_date = fields.Datetime(default=lambda self: fields.Datetime.now())
    to_date = fields.Datetime(default=lambda self: fields.Datetime.now())

    def action_print_report(self):
        from_date = self.from_date,
        to_date = self.to_date

        sale_orders = self.env['sale.order'].search([
            ('date_order', '>=', self.from_date),
            ('date_order', '<=', self.to_date),
            ('is_booking', '=', True)
        ])

        # Membuat file Excel dalam memory
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        # Add a bold format for the header
        bold = workbook.add_format({'bold': True})
        # Add a border format for the cells
        border = workbook.add_format({'border': 1})

        # Menulis header
        headers = ['Order ID', 'Customer', 'Order Date', 'Total Amount', 'Status']
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, bold)

        # Menulis data sale order
        row_num = 1
        for order in sale_orders:
            worksheet.write(row_num, 0, order.name, border)
            worksheet.write(row_num, 1, order.partner_id.name, border)
            worksheet.write(row_num, 2, str(order.date_order), border)
            worksheet.write(row_num, 3, order.amount_total, border)
            worksheet.write(row_num, 4, order.state, border)
            row_num += 1

        workbook.close()

        # Mengonversi file Excel ke base64
        file_data = base64.b64encode(output.getvalue())
        output.close()

        # Membuat attachment
        attachment = self.env['ir.attachment'].create({
            'name': 'Sale Order Report.xlsx',
            'type': 'binary',
            'datas': file_data,
            'store_fname': 'sale_order_report.xlsx',
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        # Return action untuk mendownload file
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'self',
        }
