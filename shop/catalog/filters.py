import django_filters
from django import forms
from shop.catalog.models import Product, Brand


def brands(request):
    category = request.category
    return category.brand_set.all()


class ProductFilter(django_filters.FilterSet):
    brands = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = {'price': ['exact', 'gte', 'lte'],
                  'size': ['exact']
                 }