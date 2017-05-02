# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Category (models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __unicode__(self):
        return self.name

    def is_parent(self):
        return self.parent is None

    def is_leaf(self):
        return self.parent is not None

    def get_absolute_url(self):
        return reverse('shop:products-by-category', args=[self.slug])


class Product (models.Model):
    category = models.ForeignKey(Category, verbose_name='Category')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.CharField(max_length=6)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name='Available')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product-details', args=[self.id])

