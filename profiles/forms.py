from django import forms
from .models import UserAddress


class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode', 'country',
                   'is_primary',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        self.fields['country'].widget.attrs['class'] = 'stripe-style-input'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['postcode'].widget.attrs['placeholder'] = 'Postcode'
        self.fields['town_or_city'].widget.attrs['placeholder'] = 'Town or City'
        self.fields['street_address1'].widget.attrs['placeholder'] = 'Street Address 1'
        self.fields['street_address2'].widget.attrs['placeholder'] = 'Street Address 2'
        self.fields['county'].widget.attrs['placeholder'] = 'County'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = ''
            self.fields['is_primary'].label = 'Tick to set as primary address'

class MakePrimaryForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('is_primary',)
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)       
        
        self.fields['is_primary'].widget.attrs['class'] = 'stripe-style-input'
        self.fields['is_primary'].label = 'Tick to set as primary address'
