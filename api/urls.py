from rest_framework.routers import DefaultRouter
from api.views import BookReviewsViewSet

app_name = "api"

router = DefaultRouter()
router.register('reviews', BookReviewsViewSet, basename='review')
urlpatterns = router.urls
