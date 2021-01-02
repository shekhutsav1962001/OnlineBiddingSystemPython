from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('additem',views.additem,name="additem"),
    path('biditem',views.biditem,name="biditem"),
    path('validate',views.validate,name="validate"),
    path('item/biditem',views.biditem,name="biditem"),
]