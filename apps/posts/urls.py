from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIView

router = DefaultRouter()
router.register('', PostAPIView, basename='post')

urlpatterns = router.urls
