import django_filters

from shop.catalog.models import Product


class ProductFilter(django_filters.FilterSet):
    size = django_filters.ModelMultipleChoiceFilter(Product, queryset=Product.objects.all())
    class Meta:
        model = Product
        fields = {'brand': ['exact', 'icontains'],
                  'price': ['exact', 'gte', 'lte'],
                  'size': ['exact']
                 }