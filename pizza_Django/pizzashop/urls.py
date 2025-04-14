from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", index),
    path('menu/', menu),
    path('basket/', basket),
    path('put_to_basket/<int:product_id>/', add_to_basket)
]
