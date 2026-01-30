from .views import StudentViewSet, UnitViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Student', StudentViewSet, basename='Students')
router.register(r'Unit', UnitViewSet, basename='Units')

urlpatterns = router.urls

