from django.urls import  path
from Api import  views

urlpatterns = [
    path('', views.getTask),
    path('add/', views.addTask),
    path('edit/<int:id>', views.putTask),
    path('delete/<int:id>', views.deleteTask),
]