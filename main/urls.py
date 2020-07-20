from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('search', views.main_search, name ='search'),
    path('post', views.main_post, name ='post'),
    path('template', views.main_template, name ='template'),
    path('interest', views.main_interest, name ='interest'),
    path('profile', views.main_profile, name ='profile'),
    path('ranking', views.main_ranking, name ='ranking'),
    path('alrim', views.main_alrim, name ='alrim'),
    path('friend', views.main_friend, name ='friend'),
]