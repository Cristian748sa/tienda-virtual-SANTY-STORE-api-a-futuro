from django.shortcuts import render
from products.models import Product
from django.shortcuts import redirect, get_object_or_404
from .models import Cart 
from .utils import get_or_create_cart
from .models import CartProducts


def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {
       
        'cart':cart
    })

def add(request):
    
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
   
    quantity = int(request.POST.get('quantity', 1))


    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=product, quantity=quantity)
  
    product = Product.objects.get(pk=request.POST.get('product_id'))
  
    cart.products.add(product)

    return render(request, 'carts/add.html', {
        'quantity': quantity,
        'product': product,
        'cp': cart_product
    })

def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
  
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')