from rest_framework import serializers

from posts.models import Post, Group, Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    group = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Group.objects.all(),
                                         required=False)
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
