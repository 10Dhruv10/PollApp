from django.shortcuts import render, redirect
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
