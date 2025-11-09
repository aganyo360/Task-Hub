from django.shortcuts import render, redirect
from .models import ToDoTask

# Create your views here.
def index(req):
    task= ToDoTask.objects.all()
    return render(req, "todoapp/index.html", {'task':task})

def task_list(req):
    task = ToDoTask.objects.all()
    task_count = len(task.values())
    return render(req,"todoapp/list_task.html", {'task':task, 'task_count':task_count})

def add_task(req):
    if req.method =="POST":
        title = req.POST['title']
        description = req.POST['description']
        task = ToDoTask.objects.create(title=title, description=description)
        task.save()
        return redirect('task_list')
    return render(req, "todoapp/add_task.html")

    
def complete_task(req, id):
    task = ToDoTask.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect("task_details", id=task.id)
    

def task_details(req, id):
    task = ToDoTask.objects.get(id=id)
    print(req)
    return render(req, "todoapp/task_details.html", {"task":task})

def delete_task(req, id):
    task = ToDoTask.objects.get(id=id)
    task.delete()
    return redirect('task_list')

def update_task(req, id):
    task = ToDoTask.objects.get(id=id)
    if req.method =='POST':
        task.title= req.POST.get('title')
        task.description= req.POST.get('description')
        task.save()
        return redirect("task_details",id= task.id)
    return render(req, "todoapp/update_task.html", {'task': task})
