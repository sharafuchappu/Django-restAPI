from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='post-api'),
]
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = router.urls
