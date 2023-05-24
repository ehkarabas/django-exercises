from .views import UserCreateView, UserView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView

# url(r'^rest-auth/', include('rest_auth.urls'))

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls'))
]

# ---------- Router ----------

router = DefaultRouter()
# hepsini kaplayan url'ler altta yer almali, aksi halde diger url'ler calismaz.
# ./ url'si ./someOtherUrlPart url'sini kapsayacagindan altinda yer almalidir.
router.register('create', UserCreateView)  # permissions.AllowAny
router.register('', UserView)  # permissions.IsAdminUser

urlpatterns += router.urls
