from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("search/", views.search),
    path("bait/", views.bait),
    path("rods/", views.rods),
    path("nets/", views.nets),
    path("cart/", views.cart),
    path("products/", views.products),
    ]