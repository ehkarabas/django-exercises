
# ---------- Router ----------
"""
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserView
router = DefaultRouter()
router.register('register', UserCreateView, basename='create-user') # permissions.AllowAny
router.register('list', UserView) # permissions.IsAdminUser

from django.urls import path, include

# after '/account/' -> 
urlpatterns = [
    path('auth/',include("dj_rest_auth.urls"))
]

urlpatterns += router.urls
"""

from django.urls import path, include
from .views import UserCreateView, UserView, api_root
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', UserCreateView, basename='create-user')
router.register('list', UserView, basename='user')

urlpatterns = [
    path('', api_root),
    path('auth/', include("dj_rest_auth.urls")),
] + router.urls

# urlpatterns = [
#     path('', api_root, name='api_root'),
#     path('register', UserCreateView.as_view({'post': 'create'}), name='user-register'),
#     path('list', UserView.as_view({'get': 'list'}), name='user-list'),
#     path('create', UserView.as_view({'post': 'create'}), name='user-create'),
#     path('update/<int:pk>', UserView.as_view({'put': 'update'}), name='user-update'),
#     path('partial-update/<int:pk>', UserView.as_view({'patch': 'partial_update'}), name='user-partial-update'),
#     path('destroy/<int:pk>', UserView.as_view({'delete': 'destroy'}), name='user-destroy'),
#     path('auth/', include("dj_rest_auth.urls"), name='rest_login'),
# ]

# id tanimlanmadiginda asagidaki sekilde sagliksiz calisir(update,patch,delete instance ozelinde degil tum model ozelinde olur)
# urlpatterns = [
#     path('', api_root),
#     path('register', UserCreateView.as_view({'post': 'create'}), name='create-user-list'),
#     path('list', UserView.as_view({
#         'get': 'list',
#         # 'post': 'create',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name='user-list'),
#     path('auth/', include("dj_rest_auth.urls")),
# ]