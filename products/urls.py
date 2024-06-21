from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('eulogy/',views.eulogy, name='eulogy'),
    path('vows/', views.vows, name='vows'),
    path('spouse/', views.spouse, name='spouse'),
    path('parent/', views.parent, name='parent'),
    path('weddingparty/', views.weddingparty, name='weddingparty'),
    path('anniversary/', views.anniversary, name='anniversary'),
    path('birthday/', views.birthday, name='birthday'),
    path('retirements/', views.retirements, name='retirements'),
    path('occasions/', views.occasions, name='occasions'),
    path('', views.index, name='products'),
]
