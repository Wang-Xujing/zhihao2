from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('seven/', views.sevenView.as_view(), name='seven'),
    path('first/', views.firstView.as_view(), name='first'),
    path('first_visual/', views.first_visual.as_view(), name='first_visual'),
    path('xipu/', views.xipu.as_view(), name='xipu'),
    path('count_year/', views.count_year.as_view(), name='count_year'),
]
