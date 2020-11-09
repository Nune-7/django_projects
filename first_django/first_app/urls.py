from django.urls import path
from .views import home
from .views import last_name
from .views import date_time
from .views import task
from .views import start
urlpatterns = [
    path('', home, name= "home"),
    path('name_last/', last_name, name= "last_name"),
	path('date_time/',date_time, name= "date_time"),
	path('start/', start, name= "start"),
]