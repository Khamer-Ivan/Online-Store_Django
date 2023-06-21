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


class SortForm(forms.Form):
    sort_form = forms.TypedChoiceField(label='Сортировать:',
                                       choices=[
                                           ('ПУ', 'По умолчанию'),
                                           ('ДТ', 'По дате'),
                                           ('ДЕД', 'От дешевых к дорогим'),
                                           ('ДОД', 'От дорогих к дешевым')
                                       ]
                                       )
