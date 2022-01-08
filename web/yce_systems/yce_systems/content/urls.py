from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='manifest'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
]