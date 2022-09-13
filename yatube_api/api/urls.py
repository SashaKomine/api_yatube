from rest_framework.routers import  DefaultRouter
from django.urls import path, include
from .views import CommentViewSet, GroupViewSet, PostViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments//$', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
