from django.urls import path
from . import views
from django.conf.urls import  url

urlpatterns = [
    #path('login_user', views.login_user, name="login"),

    url('login_user/', views.login_user, name="login"),


]