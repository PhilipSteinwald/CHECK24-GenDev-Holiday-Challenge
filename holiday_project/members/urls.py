from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('response/', views.resp),
    path('setup/', views.hotel_setup),
    #path('setup2/', views.offers_setup),
    path('test/', views.test_setup),
    path('testC/', views.cleanup),
]