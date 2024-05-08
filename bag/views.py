from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product



def bag(request):
    """ View to render the shopping bag page"""
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    messages.success(request,"Item added to bag")
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ To change the quantity of the specified product in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')


    request.session['bag'] = bag

    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    """ To remove a specified product from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag
    messages.success(request,f'Removed {product.name} from your bag')
    
    return HttpResponse(status=200)
    
        


