# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand
from shop.cart.forms import CartAddProductForm


def products_list(request, category_slug=None, brand_id=None):
    category = None
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    brand_id = request.GET.get('brand')
    if brand_id:
        brand_id = int(brand_id)
        products = products.filter(brand_id=brand_id)
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, 'catalog/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'brands': brands,
        'brand_id': brand_id,
    })


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/details.html', {
        'product': product,
        'cart_product_form': cart_product_form,
    })