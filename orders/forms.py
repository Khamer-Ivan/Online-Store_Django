from django import forms

from my_store_app.models import Order


class PaymentForm(forms.Form):
    numero1 = forms.CharField(max_length=10)


class OrderStepOneForm(forms.ModelForm):

    """
    Форма первого шага выполнения заказа.
    Добавление имени, фамилии, телефона и электронной почты
    к информации о заказе.
    """

    class Meta:
        model = Order
        fields = ['fio', 'phone', 'email']


class OrderStepTwoForm(forms.ModelForm):

    """
    Форма второго шага выполнения заказа.
    Добавление типа доставки, города и адреса
    к информации о заказе.
    """

    class Meta:
        model = Order
        widgets = {
            'delivery': forms.RadioSelect(
                attrs={
                    'class': 'toggle-box'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-textarea'
                }
            )
        }
        fields = ['delivery', 'city', 'address']


class OrderStepThreeForm(forms.ModelForm):

    """
    Форма третьего шага выполнения заказа.
    Добавление способа оплаты
    к информации о заказе.
    """

    class Meta:
        model = Order
        widgets = {
            'payment_method': forms.RadioSelect(
                attrs={
                    'class': 'toggle-box'
                }
            ), }
        fields = ['payment_method']
