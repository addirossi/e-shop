# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shop.catalog.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='Name', max_length=50)
    last_name = models.CharField(verbose_name='Last Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(verbose_name='Address', max_length=250)
    city = models.CharField(verbose_name='City', max_length=100)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)
    paid = models.BooleanField(verbose_name='Paid', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity