from rest_framework import generics

from Todo import models
from .serializers import TodoSerializer, DetailTodoSerializer, DetailCommentSerializer, CommentsSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()    
    serializer_class = DetailTodoSerializer
    
class ListComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = CommentsSerializer

class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = DetailCommentSerializer
    

