from django import forms

from my_store_app.models import Reviews, Product


class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['text']


class QueryForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title']
