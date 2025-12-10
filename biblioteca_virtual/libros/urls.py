from rest_framework.routers import DefaultRouter
from .views import LibroViewSet
router = DefaultRouter()

router.register(r'', LibroViewSet, basename='libro')

urlpatterns = router.urls
