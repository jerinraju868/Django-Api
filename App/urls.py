from django.urls import path
from App import  views

urlpatterns = [
    path('',views.home, name='home'),
    path('create', views.create, name='create'),
    path('edit/<int:id>', views.update, name='update'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]