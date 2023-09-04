from django.db.models import Sum, F
from slick_reporting.generator import Chart
from slick_reporting.views import SlickReportView
from .models import Sales


class SalesReport(SlickReportView):
    report_model = Sales
    date_field = 'date_of_sale'
    columns = ['product__name', 'total_sales']


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
