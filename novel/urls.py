from django.urls import path
from . import views

app_name = 'novel'

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:node_id>/',views.detail,name='node_detail'),
    path('<int:node_id>/vote/',views.vote, name='node_vote'),
]