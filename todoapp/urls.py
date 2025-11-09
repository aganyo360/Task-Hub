from django.urls import path
from . import  views

urlpatterns =[
    path('', views.index, name="index"),
    path('task_list', views.task_list, name='task_list'),
    path('task_details<int:id>', views.task_details, name='task_details'),
    path('add_task', views.add_task, name= "add_task"),
    path('complete/<int:id>', views.complete_task, name= "complete_task"),
    path('delete/<int:id>', views.delete_task, name= "delete_task"),


]