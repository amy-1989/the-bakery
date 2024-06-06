from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Product, Category, Rating, Comment
from .forms import ProductForm, RatingForm, CommentForm

def products(request):
    """ View to display all products, including searching and filtering"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to display product detail page, including product ratings,
        and comments on products"""

    product = get_object_or_404(Product, pk=product_id)
    ratings = product.ratings.all()
    average_rating = ratings.aggregate(avg=Avg('rating'))
    comments = product.comments.filter(parent__isnull=True).order_by("created_on")
    comment_count = product.comments.count()

    if request.method == "POST":

        rating_form = RatingForm(data=request.POST)

        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.author = request.user
            rating.rated_product = product
            rating.save()
            messages.success(request, "Product review added successfully!")
            return HttpResponseRedirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, "Error adding review! Please check your form and try again!")
            rating_form = RatingForm()
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except TypeError:
                parent_id = None
                print('There is no parent id! This will be a new comment!')
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent = parent_obj
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
            messages.success(request, "Comment added successfully!")
            return HttpResponseRedirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, "Error adding comment! Please try again!")
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
        rating_form = RatingForm()
 
    context = {
        'product': product,
        'rating_form': rating_form,
        'ratings': ratings,
        'average_rating': average_rating,
        'comment_count': comment_count,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def delete_rating(request, rated_product_id, id):
    """ Delete a review from the product detail """

    rating = get_object_or_404(Rating, id=id)

    if request.user == rating.author:
        rating.delete()
        messages.success(request, 'Product rating deleted!')
    else:
        messages.ERROR(request, 'You can only delete your own product ratings!')
        
    product_detail_url = reverse('product_detail', args=[rated_product_id])
    return HttpResponseRedirect(product_detail_url)


def comment_delete(request, product_id, comment_id):
    """
    view to delete comment
    """

    comment = get_object_or_404(Comment, comment_id=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')
    
    product_detail_url = reverse('product_detail', args=[product_id])

    return HttpResponseRedirect(product_detail_url)


def reply_delete(request, product_id, reply_id):
    """
    view to delete a reply
    """
    
    reply = get_object_or_404(Comment, reply_id=reply_id)

    if reply.author == request.user:
        reply.delete()
        messages.success(request, 'Reply deleted!')
    else:
        messages.error(request,
                             'You can only delete your own replies!')

    product_detail_url = reverse('product_detail', args=[product_id])

    return HttpResponseRedirect(product_detail_url)
