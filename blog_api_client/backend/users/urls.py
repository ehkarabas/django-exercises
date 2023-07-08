from django.urls import path,include
from .views import RegisterView, logout, MyPasswordResetConfirmView
from django.views.generic.base import TemplateView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('auth/logout/',logout),
    path('auth/password/reset/confirm/<slug:uidb64>/<slug:token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', TemplateView.as_view(template_name='users/pw_reset_complete.html'), name='password_reset_complete'),
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
]