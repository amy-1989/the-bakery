from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import UserProfile, UserAddress
from checkout.models import Order
from .forms import AddressForm
from django.contrib import messages


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_address = profile.address.all()    

    if request.method == 'POST':
        form = AddressForm(data = request.POST)

        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.profile = profile
            address.save()
            messages.success(request, 'Profile updated successfully')
        

    form = AddressForm()
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'user_address': user_address,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, order_number):
    """ to view the users previous order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def address(request):
    """ Display the user's saved addresses. """

    profile = get_object_or_404(UserProfile, user=request.user)
    user_address = profile.address.all() 
       

    template = 'profiles/address.html'
    context= {
        'user_address': user_address,
        'profile': profile,
    }

    return render(request, template, context)

def set_primary_address(request, id):
    """A view to allow users to change which address is their default address"""
 
    UserAddress.objects.filter(user=request.user, is_primary=True).update(is_primary=False)
    UserAddress.objects.filter(user=request.user, id=id).update(is_primary=True)
    
    return redirect (reverse('profile_address'))

