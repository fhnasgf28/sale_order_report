from odoo import models, fields, api


class WizardBookingOrderPdf(models.TransientModel):
    _name = 'booking.report.wizardpdf'
    _description = 'Wizard Booking Order PDF'

    from_date = fields.Date(default=lambda self: fields.Datetime.now())
    to_date = fields.Date(default=lambda self: fields.Datetime.now())

    def action_print_report(self):
        report = []
        from_datee = self.from_date
        to_datee = self.to_date
        if from_datee:
            report.append(('date_booking', '>=', from_datee))
        if to_datee:
            report.append(('date_booking', '<=', to_datee))

        finished_report = self.env['sale.order'].search(report)

        data = {
            'form': self.read()[0],
            'docs': finished_report,
        }

        report_action = self.env.ref('report_sale_order_inherit.report_booking_order_wizard_pdf').report_action(self, data=data)
        report_action['close_on_report_download'] = True
        return report_action
