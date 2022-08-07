from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=id)
        return post.comments

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied()
        serializer.save(author=self.request.user)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied()
        serializer.delete()
