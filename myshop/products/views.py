from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_detail.html', {'product': product})