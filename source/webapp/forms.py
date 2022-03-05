from django import forms

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }