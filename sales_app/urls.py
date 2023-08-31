from django.urls import path
from .views import SalesReport, CustomerSalesReport, MonthlySalesReport

urlpatterns = [
    path("product-sales/", SalesReport.as_view(), name="product-sales"),
    path("customer-sales/", CustomerSalesReport.as_view(), name="customer-sales"),
    path("monthly-sales/", MonthlySalesReport.as_view(), name="monthly-sales"),
]
