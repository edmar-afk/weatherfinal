from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('predict_weather', views.predict_weather, name='predict_weather'),
]