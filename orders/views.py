from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from .forms import PaymentForm


class OrderView(View):
    def get(self, request: HttpRequest):
        return render(request, 'orders/order.html')


class PaymentView(View):
    def post(self, request: HttpRequest):
        form = PaymentForm(request.POST)
        return render(request, 'orders/payment.html', {'form': form})


class PaymentProgressView(View):
    def get(self, request: HttpRequest):
        card = request.GET.get('numero1')
        number = []
        for i in card:
            if i != ' ':
                number.append(i)
        num = (number[-1])
        return render(request, 'orders/progressPayment.html', {'num': num})


class PaymentControlView(View):
    def get(self, request: HttpRequest, num):
        if int(num) != 0 and int(num) % 2 == 0:
            return redirect('orders:success')

        else:
            return redirect('orders:not_success')


def payment_success(request: HttpRequest):
    """
    Представление удачной оплаты

    ::Страница: Оплата заказа
    """
    return render(request, 'orders/success.html')


def payment_not_success(request: HttpRequest):
    """
    Представление неудачной оплаты

    ::Страница: Оплата заказа
    """
    return render(request, 'orders/not_success.html')


def order_step_1(request: HttpRequest):
    return render(request, 'orders/order_step_1.html')


def order_step_2(request: HttpRequest):
    return render(request, 'orders/order_step_2.html')


def order_step_3(request: HttpRequest):
    return render(request, 'orders/order_step_3.html')


def order_step_4(request: HttpRequest):
    return render(request, 'orders/order_step_4.html')
