from django.urls import path
from . import views

urlpatterns = [
  path('p5/', views.p5, name='p5'),
  path('p1/', views.p1, name='p1'),
  path('p2/', views.p2, name='p2'),
  path('p3/', views.p3, name='p3'),
  path('p4/', views.p4, name='p4'),
    path('', views.index, name='index'),
]