
# ------------------------------------
# Routers
# ------------------------------------

from .views import UserView, UserCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('create', UserCreateView, basename='create-user')
router.register('list', UserView)

from django.urls import path, include

# after '/user/' -> 
urlpatterns = [
    path('auth/',include("dj_rest_auth.urls"))
]

urlpatterns += router.urls