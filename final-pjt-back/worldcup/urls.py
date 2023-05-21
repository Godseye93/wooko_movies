from django.urls import path

from . import views

app_name = 'worldcup'

urlpatterns = [
    path('', views.index, name='index'),
]
