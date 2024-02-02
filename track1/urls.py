from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'track-home'),
    path('info/', views.about, name = 'track-info'),
]
