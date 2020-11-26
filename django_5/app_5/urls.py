from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_task/', views.new_task, name='new_task'),
    path('task_view/<str:pk>', views.task_view, name='task_view'),
    path('task_update/<str:pk>', views.task_update, name='task_update'),
    path('task_delete/<str:pk>', views.task_delete, name='task_delete'),
]
