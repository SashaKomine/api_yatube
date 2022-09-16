from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import permissions

from django.shortcuts import get_object_or_404

from posts.models import Post, Group
from .serializers import CommentSerializer, PostSerializer, GroupSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Доступ к объектам модели Post."""

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    premissions_classes = (IsAuthorOrReadOnly, permissions
                           .IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer_class):
        if serializer_class.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!')
        super().perform_update(serializer_class)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!')
        super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Доступ к объектам модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Доступ к объектам модели Comment."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получение конкретного объекта модели."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!')
        super().perform_destroy(instance)
