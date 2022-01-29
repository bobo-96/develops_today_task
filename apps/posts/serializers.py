from rest_framework import serializers

from apps.posts.models import Post, Comment
from apps.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author_name = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'link',
            'creation_date', 'amount_of_upvotes',
            'author_name',
        ]
        read_only_fields = [
            'amount_of_upvotes', 'creation_date'
        ]

    def create(self, validated_data):
        user = self.context.get('request').user
        post = Post.objects.create(author_name=user, **validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'author_name',
            'content', 'creation_date'
        ]
        read_only_fields = [
            'post', 'author_name', 'creation_date'
        ]



