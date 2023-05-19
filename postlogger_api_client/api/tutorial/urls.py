from .views import TutorialView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tutorials', TutorialView)
urlpatterns = router.urls
