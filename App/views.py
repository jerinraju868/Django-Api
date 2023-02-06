from django.shortcuts import render, redirect
from .models import TodoList

def home(request):
    tasks = TodoList.objects.all()

    return render(request, 'home.html', {'tasks':tasks})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        task = TodoList.objects.create(title=title, description=description)
        task.save()
        return redirect('home')
    
    else:
        return render(request, 'create.html')

def edit(request, id):  
    task = TodoList.objects.get(id=id)  
    return render(request,'edit.html', {'task':task})  


def update(request, id):
    task = TodoList.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        task = TodoList(id=id, title=title, description=description)
        task.save()
        return redirect('home')
    
    return render(request, 'edit.html',{'task':task})

def delete(request, id):
    task = TodoList.objects.filter(id=id).delete()
    return redirect('home')
    