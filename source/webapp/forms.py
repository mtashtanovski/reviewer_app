from django import forms

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'grade']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }
