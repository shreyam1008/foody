from django import forms

from .models import Food

class FoodCreateForm(forms.ModelForm):

    class Meta:
        models = Food
        fields = [
            'restaurant',
            'name',
            'price',
        ]
