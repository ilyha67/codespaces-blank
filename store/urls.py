from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('extension/<slug:slug>/', views.extension_detail, name='detail'),
    path('search/', views.search, name='search'),
    path('download/<slug:slug>/', views.download_extension, name='download'),
]