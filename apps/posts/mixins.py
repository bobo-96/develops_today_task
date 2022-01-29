from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.posts.models import Comment
from apps.posts.serializers import CommentSerializer


class CommentMixin:
    @action(detail=True, methods=['get', 'post'], serializer_class=CommentSerializer)
    def comments(self, request, *args, **kwargs):
        if self.request.method == 'GET':
            post = self.get_object()
            comments = post.post_comment.filter(post=post)
            serializer = CommentSerializer(comments, many=True)

            return Response(serializer.data)

        if self.request.method == 'POST':
            post = self.get_object()
            serializer = CommentSerializer(data=request.data)
            current_site = get_current_site(request).domain
            if serializer.is_valid():
                user = request.user
                content = serializer.data['content']
                Comment.objects.create(post=post, author_name=user, content=content)
                return HttpResponseRedirect(redirect_to=f'http://{current_site}/api/posts/{post.id}/comments/')


class UpvoteMixin:
    @action(detail=True, methods=['get'])
    def upvote(self, request, *args, **kwargs):
        post = self.get_object()
        post.upvote
        post.save()
        return Response(self.get_serializer_class()(post).data)
