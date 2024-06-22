from django.urls import path
from . import views
from .views import BlogHome

urlpatterns = [
   # path('', views.post_list, name='post_list'),
   # path('<int:pk>/', views.post_detail, name='post_detail'),
    path('', BlogHome.as_view(), name='blog'),
]
