from django import forms
from .models import Product, Category, Rating, Comment


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


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Comment here !',
                        'rows': 4, 'cols': 50}))

    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            