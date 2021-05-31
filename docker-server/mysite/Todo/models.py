from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=200)
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    class Meta:
        ordering=['created_at'] #정렬 기준

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    contents = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todo_id = models.ForeignKey('Todo', related_name='comment', null=True, blank=True, on_delete=models.CASCADE, db_column="todo_id")
    
    class Meta:
        ordering=['created_at'] #정렬 기준
