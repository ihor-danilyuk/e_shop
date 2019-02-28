from django.urls import path, include
from .views import index, show_product

urlpatterns = [
    path('', index),
    path('product/', show_product)
]
