import django_filters

from shop.catalog.models import Product


class ProductFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        size = django_filters.ModelChoiceFilter(Product,queryset=Product.objects.all())
    class Meta:
        model = Product
        fields = {'brand': ['exact', 'icontains'],
                  'price': ['exact', 'gte', 'lte'],
                  'size': ['exact']
                 }