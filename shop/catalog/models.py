# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Category (models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:products-by-category', args=[self.slug])


class Brand (models.Model):
    brand = models.CharField(max_length=50)

    def __unicode__(self):
        return self.brand

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('shop:products-by-brand', args=[self.id])


class Product (models.Model):
    category = models.ForeignKey(Category, verbose_name='Category')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    brand = models.ForeignKey(Brand, related_name='products', blank=True, null=True)
    size = models.CharField(max_length=2, blank=True)
    color = models.CharField(max_length=20, blank=True)
    price = models.PositiveIntegerField()
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