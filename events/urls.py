from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get_city/', views.get_city, name='city'),
    path('event/<int:id>/', views.event_details, name='details'),
    path('event/create/', views.create, name='create'),
    path('tinymce/', include('tinymce.urls'))
]
