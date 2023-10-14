from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/', views.coin, name='about'),
    path('get-coin/', views.get_all_coin, name='about'),
]