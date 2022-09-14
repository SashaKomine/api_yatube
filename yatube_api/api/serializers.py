from rest_framework import serializers
from rest_framework import exceptions

from posts.models import Post, Group, Comment
from .views import PostViewSet, GroupViewSet, CommentViewSet


class PostSerializer(serializers.ModelSerializer):
    group = serializers.GroupSerializer(many=False)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')
        model = Post

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)
    
    def perform_destroy(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def create(self, validated_data):
        if 'group' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post

        group_data = validated_data.pop('group')
        group = Group.objects.get_or_create(group_data)
        post = Post.objects.create(**validated_data)
        post.group = group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment
