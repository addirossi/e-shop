from django.shortcuts import render

from shop.catalog.models import Category, Product


def index(request):
    categories = Category.objects.all()
    products = Product.objects.prefetch_related('offers').filter(available=True, offers__offer_name__exact='Latest deals')
    featured = Product.objects.prefetch_related('offers').filter(available=True, offers__offer_name__exact='Featured products')
    sales = Product.objects.prefetch_related('offers').filter(available=True, offers__offer_name__exact='Sales')
    return render(request, 'index.html', locals())