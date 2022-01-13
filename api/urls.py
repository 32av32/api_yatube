from django.urls import path, include
from .views import PostApi, CommentApi, CommentDetailApi, GroupApi, FollowApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostApi)
router.register('group', GroupApi)
router.register('follow', FollowApi)


urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', CommentApi.as_view()),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentDetailApi.as_view()),
]
