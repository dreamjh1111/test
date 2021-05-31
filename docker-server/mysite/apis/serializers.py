from rest_framework import serializers
from Todo.models import Comment
from Todo.models import Todo


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'todo_id',
            'contents',
        )
        model = Comment

class DetailCommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'contents',
            'created_at',
            'updated_at',
        )
        model = Comment


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'is_completed',
        )
        model = Todo

class DetailTodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'descriptions',
            'is_completed',
            'created_at',
            'updated_at',
        )
        model = Todo


class CommentsSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'title',
            'descriptions',
            'is_completed',
            'created_at',
            'updated_at',
            'comment',
        )
        model = Todo
