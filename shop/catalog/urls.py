from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products_list, name='products-list'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.products_list, name='products-by-category'),
    url(r'^brand/(?P<brand_id>\d+)/$', views.products_list, name='products-by-brand'),
    url(r'^products/(?P<product_id>\d+)/$', views.product_details, name='product-details'),
]