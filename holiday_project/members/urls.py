from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('response/', views.test_resp),
    path('result/', views.test_result),
    path('final/', views.test_final),
    path('setup/', views.hotel_setup),
    path('test/', views.test_setup),
]