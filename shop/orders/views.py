# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from shop.catalog.models import Category
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import OrderCreated
from shop.cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            OrderCreated(order.id)
        return render(request, 'orders/order/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/order/checkout.html', {'cart': cart,
                                                        'form': form,
                                                        'categories': categories,})


