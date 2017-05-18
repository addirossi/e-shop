# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from shop.cart.forms import CartAddProductForm


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'catalog/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/details.html', {
        'product': product,
        'cart_product_form': cart_product_form,
    })