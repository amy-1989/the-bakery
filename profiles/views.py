from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import UserProfile, UserAddress, User, FeedbackForm
from checkout.models import Order
from .forms import AddressForm, CustomerFeedbackForm
from django.contrib import messages


@login_required
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
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
        

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

@login_required
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

@login_required
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

@login_required
def set_primary_address(request, id):
    """A view to allow users to change which address is their default address"""
 
    UserAddress.objects.filter(user=request.user, is_primary=True).update(is_primary=False)
    UserAddress.objects.filter(user=request.user, id=id).update(is_primary=True)
    
    return redirect (reverse('profile_address'))

@login_required
def edit_address(request, id=None):
    """ a view to allow users to edit their saved addresses"""
   
    addresses = UserAddress.objects.all()

    if id:
        address = get_object_or_404(UserAddress, id=id)
        address_form = AddressForm(instance=address)
    else:
        address_form = AddressForm()

    if request.method == 'POST':
        if id:
            address = get_object_or_404(UserAddress, id=id)
            address_form = AddressForm(request.POST,
                                       request.FILES, instance=address)
        else:
            address_form = AddressForm(request.POST, request.FILES)
        if address_form.is_valid():
            address_form.save()
            messages.success(request, "Address edited successfully!")
        return redirect (reverse('profile_address'))

    return render(request, 'profiles/edit_address.html', {
        'address': address if id else None,
        'address_form': address_form,
        'addresses': addresses
        })


@login_required
def delete_address(request, id):
    """
    view to delete addresses
    """
    address = get_object_or_404(UserAddress, id=id)

    if address.user == request.user:
        address.delete()
        messages.add_message(request, messages.SUCCESS, 'Address deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own addresses!')

    return HttpResponseRedirect('/')


@login_required
def delete_account(request, id):
    """
    view to delete user including profile
    """
    user = get_object_or_404(User, id=id)

    if user == request.user:
        user.delete()
        messages.add_message(request, messages.SUCCESS, 'Account deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own account!')

    return HttpResponseRedirect('/')


@login_required
def customer_feedback(request):
    """
    Renders the Feedback form page
    """
    feedback = FeedbackForm.objects.all()
    if request.method == "POST":
        customer_feedback_form = CustomerFeedbackForm(data=request.POST)
        if customer_feedback_form.is_valid():
            customer_feedback_form.save()
            messages.success(request, 
                "Message received! We will respond as soon as possible!")


    customer_feedback_form = CustomerFeedbackForm()

    return render(
        request,
        "profiles/feedback_form.html",
        {"customer_feedback_form": customer_feedback_form,
         "feedback": feedback}
    )


