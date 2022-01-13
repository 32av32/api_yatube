from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUserOrReadOnly


class PostApi(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentApi(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.kwargs.get('post_pk'))
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.kwargs.get('post_pk'))
        return queryset


class GroupApi(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class FollowApi(ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username', 'user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


