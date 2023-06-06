from django import forms

from my_store_app.models import Reviews


class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['text']
