from rest_framework import viewsets


from apps.posts.mixins import CommentMixin, UpvoteMixin
from apps.posts.models import Post
from apps.posts.permissions import IsPostOwnerOrReadOnly
from apps.posts.serializers import PostSerializer


class PostAPIView(viewsets.ModelViewSet, CommentMixin, UpvoteMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsPostOwnerOrReadOnly,)

