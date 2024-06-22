<<<<<<< HEAD
from django.shortcuts import render,redirect
=======
from django.shortcuts import render, redirect, reverse,  HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

>>>>>>> developer

# Create your views here.

def view_bag(request):
    """ A view that tenders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
<<<<<<< HEAD
<<<<<<< HEAD

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
=======
=======

    product = get_object_or_404(Product, pk=item_id)
>>>>>>> developer
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})
    if item_id in bag:
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
    
    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product in the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        
        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
        else:
            messages.warning(request, f'{product.name} was not in your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    
    except Exception as e:
<<<<<<< HEAD
        return HttpResponse(status=500)
>>>>>>> developer
=======
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
>>>>>>> developer
