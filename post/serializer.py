from rest_framework import serializers
from post.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализация для поста
    """

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'date',
        ]
        read_only_fields = [
            'date',
        ]
        extra_kwargs = {
            'date': {'read_only': True},
        }


class CommentCreateSerializer(serializers.ModelSerializer):
    """
    Сериализация для комментария
    """

    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'date',
            'post',
            'parent',
        ]
        read_only_fields = [
            'date',
        ]
        extra_kwargs = {
            'date': {'read_only': True},
        }

    def validate(self, data):
        """
        Валидация загружаемой комментария
        """
        if data['post'] is None and data['parent'] is None:
            raise serializers.ValidationError({"Error": "You have to choose parent"})
        elif data['post'] is not None and data['parent'] is not None:
            raise serializers.ValidationError({"Error": "You have to choose only one parent"})
        return data


class CommentViewSerializer(serializers.ModelSerializer):
    """
    Сериализация для комментария
    """

    class Meta:
        model = Comment
        fields = [
            'id',
            'level',
            'text',
            'date',
            'post',
            'parent',
        ]
        read_only_fields = [
            'date',
        ]
        extra_kwargs = {
            'date': {'read_only': True},
        }
