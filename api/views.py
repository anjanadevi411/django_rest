from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task

@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def apilistview(request):
    tasks = Task.objects.all()
    task_ser = TaskSerializer(tasks, many=True)
    return Response(task_ser.data)

@api_view(['GET'])
def apidetailview(request,pk):
    tasks = Task.objects.get(id=pk)
    task_ser = TaskSerializer(tasks, many=False)
    return Response(task_ser.data)

@api_view(['POST'])
def apicreateview(request):
    task_ser = TaskSerializer(data=request.data)
    if task_ser.is_valid():
        task_ser.save()
    return Response(task_ser.data)

@api_view(['POST'])
def apiupdateview(request,pk):
    task = Task.objects.get(id=pk)
    task_ser = TaskSerializer(instance=task, data=request.data)
    if task_ser.is_valid():
        task_ser.save()
    return Response(task_ser.data)

@api_view(['DELETE'])
def apideleteview(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item successfully deleted')