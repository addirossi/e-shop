# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from shop.offers.models import Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ['offer_name', 'offer_description', 'discount', 'expires']
    list_filter = ['expires']
    list_editable = ['discount']

admin.site.register(Offer, OfferAdmin)