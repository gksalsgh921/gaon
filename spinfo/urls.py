from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.spinfo),
    path('register_complete', views.register_complete),
    path('register', views.register),
]
