# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from shop.catalog.filters import ProductFilter
from .models import Category, Product, Brand
from shop.cart.forms import CartAddProductForm


def products_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug) if category_slug else None

    sort_field = request.GET.get('sort', 'name')
    sort_order = request.GET.get('order', 'asc')

    filtered_brands = request.GET.getlist('filter-brand', None)

    filtered_brands = [int(x) for x in filtered_brands]

    categories = Category.objects.filter(parent__isnull=True)

    products = Product.objects.filter(available=True)
    brands = Brand.objects.all()

    if filtered_brands:
        products = products.filter(brand__id__in=filtered_brands)

    if category:
        products = products.filter(category=category)
        brands = brands.filter(products__category=category)

    brands = brands.distinct()

    if sort_order == 'desc':
        sort_field = '-{}'.format(sort_field)
    products = products.order_by(sort_field)

    cart_product_form = CartAddProductForm()

    return render(request, 'catalog/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form,
        'brands': brands,
        'filtered_brands': filtered_brands,
        'sort_field': sort_field,
        'sort_order': sort_order,
        'cart_product_form': cart_product_form
    })


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/details.html', {
        'product': product,
        'cart_product_form': cart_product_form,
    })