from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginmain, name = 'loginmain'),
    path('loginprocess', views.loginprocess, name ='loginprocess'),
]