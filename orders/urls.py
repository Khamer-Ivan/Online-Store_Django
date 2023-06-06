from django.urls import path

from orders.views import (OrderView,
                          PaymentView,
                          PaymentProgressView,
                          payment_success,
                          payment_not_success,
                          PaymentControlView,
                          order_step_1,
                          order_step_2,
                          order_step_3,
                          OrderStepFour,
                          OrderHistory,
                          order_detail,)

app_name = 'orders'

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('payment_progress/', PaymentProgressView.as_view(), name='payment_progress'),
    path('control/<int:num>', PaymentControlView.as_view(), name='control'),
    path('success/', payment_success, name='success'),
    path('not_success/', payment_not_success, name='not_success'),
    path('order_step_1/', order_step_1, name='order_step_1'),
    path('order_step_2/', order_step_2, name='order_step_2'),
    path('order_step_3/', order_step_3, name='order_step_3'),
    path('order_step_4/', OrderStepFour.as_view(), name='order_step_4'),
    path('order_history/', OrderHistory.as_view(), name='order_history'),
    path('order_detail/<int:pk>', order_detail, name='order_detail'),
]
