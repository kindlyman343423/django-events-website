from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get_location/', views.get_location, name='location'),
    path('event/<int:id>/', views.event_details, name='details')
]
