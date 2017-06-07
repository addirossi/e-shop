# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from shop.catalog.models import Product


class Offer(models.Model):
    offer_name = models.CharField(max_length=50)
    offer_description = models.TextField(max_length=200)
    discount = models.PositiveIntegerField(blank=True, null=True)
    expires = models.DateField()
    products = models.ManyToManyField(Product, related_name='offers')

    def __unicode__(self):
        return self.offer_name

    def __str__(self):
        return self.offer_name