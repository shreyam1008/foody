from django import forms

from .models import Food

class FoodCreateForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = [
            'restaurant',
            'name',
            'price',
        ]
