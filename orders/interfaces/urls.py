from django.urls import path
from .views import order_status, stock_status

urlpatterns = [
    path('order-status/', order_status, name='order-status'),
    path('stock-status/', stock_status, name='stock-status'),
]
