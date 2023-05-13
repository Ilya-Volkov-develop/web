from django import forms
from .models import Product_type

class Product_typeForm(forms.ModelForm):
    class Meta:
        model = Product_type
        fields = ['title']

    labels = {'title':''}
    widgets = {'title': forms.TextInput(attrs={'class':'form-control'})}