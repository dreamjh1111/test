from django.urls import path

from .views import ListTodo, DetailTodo, ListComment, DetailComment

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('<int:pk>/comments/', ListComment.as_view()),
    path('<int:pk>/comments/<int:Comment_id>', DetailComment.as_view()),
]

