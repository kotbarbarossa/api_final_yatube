from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Comment, User
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .serializers import FollowSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

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
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=id)
        return post.comments


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        following_user = get_object_or_404(
            User,
            username=self.request.data.get("following")
        )
        serializer.save(
            user=self.request.user,
            following=following_user
        )
