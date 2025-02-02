from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm() 
    
    if request.method == "POST":
        form = TaskForm(request.POST)   #populate the form with the submitted data
        
        if form.is_valid():
            form.save()                 #save to DB
        
        return redirect('/')            #form will get resubmitted with duplicated data if user reloads page so we redirect them to home
        
    
    context = {'tasks': tasks, 'TaskForm': form}
    return render(request, 'tasks.html', context)  #we render a template

def updateTask(request, pk):
    task_object = get_object_or_404(Task, pk = pk)                 #get Model's object (it has all data) with given pk
    form = TaskForm(instance = task_object)                        #populate form with previous line object (data)

    if request.method == "POST":                                   #if user now submits form after editing -> proceed 
        form = TaskForm(request.POST, instance = task_object)      #populate form with new data at task_object and not some new object
        
        if form.is_valid():
            form.save()
        
        return redirect('/')
    
    context = {'TaskForm' : form}
    return render(request, 'update-task.html', context)

def deleteTask(request, pk):
    task_object = get_object_or_404(Task, pk =  pk)
    
    if request.method == 'POST':                                    #post request comes when we click on button to delete
        task_object.delete()
        
        return redirect('/')

    context = {'task' : task_object}
    
    return render(request, 'delete-task.html', context)