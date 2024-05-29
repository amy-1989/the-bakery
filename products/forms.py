from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            
