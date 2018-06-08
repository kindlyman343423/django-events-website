from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('api/get_location/', views.get_location, name='location'),
]
