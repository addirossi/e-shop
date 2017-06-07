# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,Product, Brand


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated', 'brand', 'size', 'color']
    list_filter = ['available', 'created', 'updated', 'brand']
    list_editable = ['price', 'stock', 'available']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
