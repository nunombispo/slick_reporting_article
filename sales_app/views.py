import csv
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from slick_reporting.generator import Chart
from slick_reporting.views import SlickReportView
from .models import Sales


class SalesReport(SlickReportView):
    report_model = Sales
    date_field = 'date_of_sale'
    columns = ['product__name', 'total_sales']

    def export_csv(self, report_data):
        """
        Export report data as CSV
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sales.csv"'
        writer = csv.writer(response)
        writer.writerow(['Product', 'Total Sales'])
        for row in report_data['data']:
            writer.writerow([row['product__name'], row['total_sales']])
        return response

    def export_pdf(self, report_data):
        """
        Export report data as PDF
        """
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sales.pdf"'

        pdf = SimpleDocTemplate(
            response,
            pagesize=A4
        )

        # Create table with your data
        table_data = [['Product', 'Total Sales']]
        for row in report_data['data']:
            table_data.append([row['product__name'], row['total_sales']])

        table = Table(table_data)

        # Add Table Style
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        elements = [table]
        pdf.build(elements)

        return response


class CustomerSalesReport(SlickReportView):
    report_model = Sales
    date_field = 'date_of_sale'
    columns = ['customer__name', 'product__name', 'total_sales']


class MonthlySalesReport(SlickReportView):
    report_model = Sales
    date_field = 'date_of_sale'
    columns = ['product__name', 'total_sales']
    chart_settings = [
        Chart(
            "Total sold $",
            Chart.BAR,
            data_source=["total_sales"],
            title_source=["product__name"],
        ),
    ]
