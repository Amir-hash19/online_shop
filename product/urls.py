from django.urls import path
from product.views import show_products_page



urlpatterns = [
    path("list-product", show_products_page),
]