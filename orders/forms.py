from django import forms


class PaymentForm(forms.Form):
    numero1 = forms.CharField(max_length=10)
