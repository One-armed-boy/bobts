from django.urls import path
from . import views

app_name = 'workspace'

urlpatterns=[
    path('', views.index, name='index'),
    path('start_write/',views.start_write, name='start_write'),
    path('<int:node_id>/',views.start_detail,name='start_detail'),
    path('<int:node_id>/modify/',views.node_modify,name='node_modify'),
    path('<int:node_id>/delete/',views.node_delete,name='node_delete'),
    path('<int:node_id>/eject/',views.node_eject,name='node_eject'),
]