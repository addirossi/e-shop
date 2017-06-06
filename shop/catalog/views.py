# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from shop.catalog.filters import ProductFilter
from .models import Category, Product, Brand
from shop.cart.forms import CartAddProductForm


def products_list(request, category_slug=None):
    category = None

    sort_field = request.GET.get('sort', 'name')
    sort_order = request.GET.get('order', 'asc')
    categories = Category.objects.filter(parent__isnull=True)

    products = Product.objects.filter(available=True)
    # brand_id = request.GET.get('brand')
    # if brand_id:
    #     brand_id = int(brand_id)
    #     products = products.filter(brand_id=brand_id)
    if category_slug:
        products = products.filter(category__slug=category_slug)
        # brands = Brand.objects.filter(products__category__slug=category_slug)

    if sort_order == 'desc':
        sort_field = '-{}'.format(sort_field)
    products = products.order_by(sort_field)

    paginator = Paginator(products, 15)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/list.html', {
        'paginator': paginator,
        'category': category,
        'categories': categories,
        'products': products,
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