from .models import ContactForm
from django import forms


class AboutContactForm(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            
