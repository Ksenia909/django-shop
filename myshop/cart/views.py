from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product
from .cart import Cart


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'show_message': True})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    action = request.POST.get('action')

    if action == 'increase':
        cart.add(product=product)
    elif action == 'decrease':
        cart.add(product=product, quantity=-1)
        if int(cart.cart[str(product.id)]['quantity']) <= 0:
            cart.remove(product)

    return redirect('cart:cart_detail')

