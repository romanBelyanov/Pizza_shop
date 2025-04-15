from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('do_order/', do_order),
    path("", index),
    path('menu/', menu),
    path('basket/put_to_basket/<int:product_id>/', add_to_basket1),
    path('basket/delete_from_basket/<int:product_id>/', delete_from_basket),
    path('basket/', basket),
    path('put_to_basket/<int:product_id>/', add_to_basket),
    path("new/new_order/", new_order),
    path('new/', new),
    path("about/", about),
    path("contacts/", contacts)
]
