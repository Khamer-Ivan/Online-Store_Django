from django.urls import path

from orders.views import OrderView

app_name = 'orders'

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
]
