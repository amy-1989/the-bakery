from django import forms
from .models import Product, Category, Rating


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('rating', 'review',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            