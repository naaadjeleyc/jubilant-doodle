from django.urls import path
from . import views
from django.conf.urls import  url

urlpatterns = [
    path('', views.store, name="store"),

    path('cart/', views.cart, name="cart"),

    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.checkout, name="update_item"),

    url('viewgraph/', views.CityChartView.as_view(), name= "view")

    

]