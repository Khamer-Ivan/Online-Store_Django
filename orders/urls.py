from django.urls import path

from orders.views import (OrderView,
                          PaymentView,
                          PaymentProgressView,
                          payment_success,
                          payment_not_success,
                          PaymentControlView,
                          )

app_name = 'orders'

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('payment_progress/', PaymentProgressView.as_view(), name='payment_progress'),
    path('control/<int:num>', PaymentControlView.as_view(), name='control'),
    path('success/', payment_success, name='success'),
    path('not_success/', payment_not_success, name='not_success')
]
