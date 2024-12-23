# from rest_framework.routers import DefaultRouter
# from .views import PostViewSet, 

# router = DefaultRouter()
# router.register('posts', PostViewSet)

# urlpatterns = router.urls

from django.urls import path
from .views import PostList, PostDetail, SignupView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('signup/', SignupView.as_view(), name='signup'),
]
