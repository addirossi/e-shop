# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.catalog.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request, 'Product added to your cart', extra_tags='success')
    return redirect('cart:cart-detail')


def cart_add_2(request, product_id):
    res = {'status': 'ok', 'redirect': True}
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request, 'Product added to your cart', extra_tags='success')
        if cd['update']:
            res['redirect'] = False
    else:
        res['status'] = 'fail'
    return JsonResponse(res)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart-detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True,
            })
    return render(request, 'cart/detail.html', {'cart': cart})