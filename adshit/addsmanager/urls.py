from django.urls import path
from . import views

app_name='addsmanager'

urlpatterns = [
    path('', views.index, name='index'),
]