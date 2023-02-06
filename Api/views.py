from rest_framework.response import Response
from rest_framework.decorators import api_view
from App.models import TodoList
from .serializer import TodoAppSerializer


@api_view(['POST'])
def addTask(request):
    serializer = TodoAppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getTask(request):
    task = TodoList.objects.all()
    serializer = TodoAppSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def putTask(request, id):
    task = TodoList.objects.get(id=id)
    if request.method == 'PUT':
        serializer = TodoAppSerializer(task, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
    return Response(serializer.data) 

@api_view(['DELETE'])
def deleteTask(request, id):
    task = TodoList.objects.get(id=id)
    if request.method == 'DELETE':
        task.delete()
    return Response()
