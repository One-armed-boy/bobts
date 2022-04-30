from django.urls import path
from . import views

app_name = 'novel'

urlpatterns=[
    path('', views.index, name='index'),
]