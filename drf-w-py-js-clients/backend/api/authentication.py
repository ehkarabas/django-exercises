from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from django.db import models

from django.utils import timezone
from datetime import timedelta


# custom Token model with a new custom method
class ExpiringToken(Token):
    class Meta:
        proxy = True

    def has_expired(self):
        return self.created < timezone.now() - timedelta(days=1)


# custom TokenAuthentication
class TokenAuthentication(BaseTokenAuth):
    keyword = "Token"
    model = ExpiringToken

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)

        if token.has_expired():
            token.delete()
            raise AuthenticationFailed("Token has expired")

        return (user, token)
