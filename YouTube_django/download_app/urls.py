from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('download/', views.download, name='download'),
    path('downloading/', views.downloading, name='downloading'),
    
] 