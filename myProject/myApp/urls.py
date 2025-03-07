from django.urls import path;
from .views import *


urlpatterns = [
    path("",home, name="home"),
    path("events", events, name="events"),
    path("add-product/",createProduct, name="product" ),
    path("view-product/", viewProduct, name="productsList"),
    path("delete-product/<str:id>/", deleteProduct, name="delete-product"),   
    path("edit-product/<str:id>/", editProduct, name="edit-product") 
]