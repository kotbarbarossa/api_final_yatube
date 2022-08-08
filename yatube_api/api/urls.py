from django.urls import include, path
from rest_framework import routers
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from rest_framework.authtoken import views

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
v1_router.register(r'follow', FollowViewSet, basename='follows'),

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
