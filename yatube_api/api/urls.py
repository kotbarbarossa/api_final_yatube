from django.urls import include, path
from rest_framework import routers
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

jwt_patterns = [
    path('create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='posts')
v1_router.register(r'groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
v1_router.register(r'follow', FollowViewSet, basename='follows'),

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/jwt/', include(jwt_patterns)),
]
