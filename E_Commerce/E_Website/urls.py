from django.urls import path

from .views import ListProducts, ListUsers, ListOrders

urlpatterns = [
    path("", ListProducts.as_view()),
    path("users/", ListUsers.as_view()),
    path("orders/", ListOrders.as_view()),
]