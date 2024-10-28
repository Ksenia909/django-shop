from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def product_list(request):
    products = Product.available_manager.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_detail.html', {'product': product})


def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.available_manager.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'category': category, 'categories': categories})