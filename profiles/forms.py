from django import forms
from .models import UserAddress, FeedbackForm


class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode', 'country',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        self.fields['country'].widget.attrs['class'] = 'stripe-style-input'
        self.fields['phone_number'].widget.attrs[
            'placeholder'] = 'Phone Number'
        self.fields['postcode'].widget.attrs['placeholder'] = 'Postcode'
        self.fields['town_or_city'].widget.attrs[
            'placeholder'] = 'Town or City'
        self.fields['street_address1'].widget.attrs[
            'placeholder'] = 'Street Address 1'
        self.fields['street_address2'].widget.attrs[
            'placeholder'] = 'Street Address 2'
        self.fields['county'].widget.attrs['placeholder'] = 'County'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = ''


class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = ('order_number',
                  'customer_name', 'email',
                  'message',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['order_number'].widget.attrs['autofocus'] = True
        self.fields['customer_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['message'].widget.attrs[
            'placeholder'] = 'Place your message here'
        self.fields['order_number'].widget.attrs[
            'placeholder'] = 'Order Number'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = ''
