from django.urls import path
from .views import apioverview,apilistview,apidetailview,apicreateview,apiupdateview,apideleteview
urlpatterns = [
    path('',apioverview,name='api_overview'),
    path('task-list/',apilistview,name='task-list'),
    path('task-detail/<str:pk>/',apidetailview,name='task-detail'),
    path('task-create/',apicreateview,name='task-create'),
    path('task-update/<str:pk>/',apiupdateview,name='task-update'),
    path('task-delete/<str:pk>/',apideleteview,name='task-delete'),
]