from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('eulogy/',views.eulogy, name='eulogy'),
    path('vows/', views.vows, name='vows'),
    path('spouse/', views.spouse, name='spouse')
]
