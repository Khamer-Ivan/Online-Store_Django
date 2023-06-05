from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from my_store_app.models import Order, Cart, ProductInOrder
from .forms import PaymentForm, OrderStepOneForm, OrderStepTwoForm, OrderStepThreeForm


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

            order = Order.objects.filter(customer=request.user, in_order=True).last()

            cart = Cart.objects.filter(username=request.user.profile)
            for product in cart:
                order.price += product.product.price * product.quantity
                ProductInOrder.objects.create(
                    user=request.user,
                    order=order,
                    product=product.product,
                    quantity=product.quantity
                )
            order.save()
            cart.delete()

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
    if request.method == 'POST':
        form = OrderStepOneForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                fio = form.cleaned_data['fio']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']

                order = Order.objects.filter(customer=request.user, in_order=False)

                if not order.exists():
                    Order.objects.create(
                        fio=fio,
                        email=email,
                        phone=phone,
                        customer=request.user
                    )

                else:
                    order = Order.objects.filter(customer=request.user, in_order=False).last()
                    order.fio = fio
                    order.email = email
                    order.phone = phone
                    order.save()

                return redirect('orders:order_step_2')
            else:
                return redirect('my_store_app:login')
    else:
        form = OrderStepOneForm()
        return render(request, 'orders/order_step_1.html', {'form': form})


def order_step_2(request: HttpRequest):
    if request.method == 'POST':
        form = OrderStepTwoForm(request.POST)
        order = Order.objects.get(customer=request.user, in_order=False)
        if form.is_valid():
            delivery = form.cleaned_data['delivery']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']

            order.delivery = delivery
            order.city = city
            order.address = address
            order.save()

            return redirect('orders:order_step_3')
    else:
        form = OrderStepTwoForm()
        return render(request, 'orders/order_step_2.html', {'form': form})


def order_step_3(request: HttpRequest):
    if request.method == 'POST':
        form = OrderStepThreeForm(request.POST)
        order = Order.objects.get(customer=request.user, in_order=False)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']

            order.payment_method = payment_method
            order.in_order = True
            order.save()

            return redirect('orders:order_step_4')
    else:
        form = OrderStepThreeForm()
        return render(request, 'orders/order_step_3.html', {'form': form})


class OrderStepFour(View):

    """
    Представление четвертого шага оформления заказа

    ::Страница: Оформление заказа
    """

    def get(self, request: HttpRequest):
        user = request.user
        if user.is_authenticated:
            order = Order.objects.filter(customer=user, in_order=True).last()
            return render(request, 'orders/order_step_4.html', {'order': order})

        else:
            return redirect('profiles:login')
