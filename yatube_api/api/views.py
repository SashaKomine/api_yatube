from rest_framework import viewsets
from rest_framework import mixins

from posts.models import Post, Group, Comment
from .serializers import CommentSerializer, PostSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RetriveListMixins(mixins.RetrieveModelMixin, mixins.ListModelMixin):
    pass


class GroupViewSet(RetriveListMixins):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
