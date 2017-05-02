from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductsList, name='products-list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductsList, name='products-by-category'),
    url(r'^(?P<product_id>\d+)/$', views.ProductDetails, name='product-details'),
]