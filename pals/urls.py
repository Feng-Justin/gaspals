from django.urls import path

from . import views

urlpatterns = [
    path('Traffic', views.traffic, name='traffic'),
    path('LGS', views.lgs, name='LGS'),
    path('Routes', views.routes, name='routes'),
    path('Statistics', views.stats, name='stats'),
    path('Profile', views.profile, name='profile'),
    path('Home', views.home, name='home'),
    path('', views.home, name='home'),
]