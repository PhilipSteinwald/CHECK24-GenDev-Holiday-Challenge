from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('response/', views.resp),
    path('result/', views.result),
    path('final/', views.final),
]