# **Django-Api**
## Create virtualenvironment and setup
    python -m venv Env
    source Env/bin/activate

## install django in virtualenvironment
    pip install django

# Create Project
    django-admin startproject Todo

## Create app
    cd Todo
    python manage.py startapp App

# setting.py

## importing package
    import os

## Add app name and rest framework in installed apps
    INSTALLED_APPS = [
        'App','rest_framework',
    ]

## Add Templates folder path
    os.path.join(BASE_DIR, 'templates')

# Create a new folder called Api in the project root directory

# Api
## Create a __init__.py file in Api folder
## Create ursl.py in Api folder
## Create views.py in APi folder
## Create serializer.py in Api folder


# App
## Create a urls.py file in App folder


# Todo/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('App.urls')),
        path('api/', include('Api.urls')),
    ]

# **App**
## Create model
### App.models.py
    from django.db import models

    class TodoList(models.Model):
        title = models.CharField(max_length=200, null=False)
        description = models.TextField()
        create_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title


# import the files and packages
## App/views.py
    from django.shortcuts import render, redirect
    from .models import TodoList

# Home page
## App/views.py
    def home(request):
        tasks = TodoList.objects.all()

        return render(request, 'home.html', {'tasks':tasks})

## templates/base.html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% block title %}
        <title>CRUD</title>
        {% endblock title %}
    </head>
    <body style="background-color:rgb(206, 206, 206)">
        
        <nav class="navbar navbar-light bg-light">
            <div style="display: flex;">
                <img src="data:image/png;base64,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" style="width: 150px; margin-left: 50px;background-color: fdfdfd;">&nbsp;&nbsp;
                <label >
                    <a class="navbar-brand" href="{% url 'home' %}" style="font-size: xx-large; font-weight: bolder; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                        CRUD APP
                    </a>
                    </label>
            </div>
        </nav>
        <br>

        {% block content %}
        {% endblock %}
        
    </body>
    </html>

## template/home.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Home</title>
    {% endblock title %}

    {% block content %}
    <div class="container">
        <div class="card shadow"  style="border-radius: 0.5rem">
            <div class="card-header">
                <h1 align="center" style="margin-top: 25px; font-family: Arial, Helvetica, sans-serif;">Home Page </label>
            </div>
            <div class="card-body">
                <p>
                    <a href="{% url 'create' %}" class="btn btn-primary">Add New Task</a>
                </p><hr>
                
            <table class="table">
                <thead>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Actions</th>
                </thead>
                <tbody>
                    {% for task in tasks %}
                    <tr>
                        <td>{{task.id}}</td>
                        <td>{{task.title}}</td>
                        <td>{{task.description}}</td>
                        <td>
                            <a href="{% url 'update' task.id %}" class="btn btn-success btn-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                                    <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                    <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                                </svg>
                            </a>
                            <a href="{% url 'delete' task.id %}" class="btn btn-danger btn-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                                    <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
                                </svg>
                            </a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            </div>
        </div>
    </div>
    {% endblock content %}


# Funtion for task creation
## App/views.py
    def create(request):
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']

            task = TodoList.objects.create(title=title, description=description)
            task.save()
            return redirect('home')
        
        else:
            return render(request, 'create.html')

## templates/create.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Home</title>
    {% endblock title %}

    {% block content %}
    <div class="container" style="display: flex;justify-content: center;">
        <div class="card shadow"  style="border-radius: 0.5rem;width: 650px;">
            <div class="card-header">
                <h1 align="center" style="margin-top: 25px; font-family: Arial, Helvetica, sans-serif;">Create Task </label>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    <input type="text" name="title" placeholder="Task Title" class="form-control" required><br><br>
                    <textarea class="form-control" name="description" placeholder="Description...." required></textarea><br>
                    <center>

                        <input type="submit" value="Add Task" class="btn btn-success">
                    </center>
                </form>
            </div>
        </div>
    </div>
    {% endblock content %}



# function for edit and upadate
## App/views.py
### edit
    def edit(request, id):  
        task = TodoList.objects.get(id=id)  
        return render(request,'edit.html', {'task':task})  

### update
    def update(request, id):
        task = TodoList.objects.get(id=id)
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']

            task = TodoList(id=id, title=title, description=description)
            task.save()
            return redirect('home')
        
        return render(request, 'edit.html',{'task':task})
## templates/edit.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Update</title>
    {% endblock title %}

    {% block content %}
    <div class="container" style="display: flex;justify-content: center;">
        <div class="card shadow"  style="border-radius: 0.5rem;width: 650px;">
            <div class="card-header">
                <h1 align="center" style="margin-top: 25px; font-family: Arial, Helvetica, sans-serif;">Update Task </label>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    <input type="text" name="title" placeholder="Task Title" value="{{task.title}}" class="form-control" required><br><br>
                    <textarea class="form-control" name="description" placeholder="Description...." required>{{task.description}}</textarea><br>
                    <center>

                        <input type="submit" value="Update Task" class="btn btn-success">
                    </center>
                </form>
            </div>
        </div>
    </div>
    {% endblock content %}


# Function for delete
## App/views.py
    def delete(request, id):
        task = TodoList.objects.filter(id=id).delete()
        return redirect('home')
        

# App/urls.py
    from django.urls import path
    from App import  views

    urlpatterns = [
        path('',views.home, name='home'),
        path('create', views.create, name='create'),
        path('edit/<int:id>', views.update, name='update'),
        path('update/<int:id>', views.update, name='update'),
        path('delete/<int:id>', views.delete, name='delete')
    ]

# App/admin.py
    from django.contrib import admin
    from App.models import TodoList

    admin.site.register(TodoList)

# Makemigration and Migrate  and runserver
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

# **Browser views**
## Home page
![Screenshot from 2023-02-06 21-45-34](https://user-images.githubusercontent.com/117073931/217025261-14ef4ef8-4040-4947-81cd-9272d36d5b88.png)
## Create Task
![Screenshot from 2023-02-06 21-46-38](https://user-images.githubusercontent.com/117073931/217025397-75af63fa-a489-4827-9522-fde10909b377.png)
## Edit Task
![Screenshot from 2023-02-06 21-47-13](https://user-images.githubusercontent.com/117073931/217025514-aae26bc4-4e20-4650-a81e-4719ca0725cc.png)


# **API**

## Api/serializer.py
    from rest_framework import serializers
    from App.models import TodoList


    class TodoAppSerializer(serializers.ModelSerializer):
        class Meta:
            model = TodoList
            fields = '__all__'

## Api/views.py
### Importing the files and packages
    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    from App.models import TodoList
    from .serializer import TodoAppSerializer

### GET 
    @api_view(['GET'])
    def getTask(request):
        task = TodoList.objects.all()
        serializer = TodoAppSerializer(task, many=True)
        return Response(serializer.data)

### POST
    @api_view(['POST'])
    def addTask(request):
        serializer = TodoAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

### PUT
    @api_view(['PUT'])
    def putTask(request, id):
        task = TodoList.objects.get(id=id)
        if request.method == 'PUT':
            serializer = TodoAppSerializer(task, data=request.data) 
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data) 
        return Response(serializer.data) 

### DELETE
    @api_view(['DELETE'])
    def deleteTask(request, id):
        task = TodoList.objects.get(id=id)
        if request.method == 'DELETE':
            task.delete()
        return Response()
