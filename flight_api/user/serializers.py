from dj_rest_auth.serializers import TokenSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # email'i zorunlu hale getir ve unique kontrolu sagla
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # passowrd'u zorunlu olmaktan cikar
    password = serializers.CharField(
        required=False,
        write_only=True,
    )

    class Meta:
        model = User
        exclude = [
            # "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]

    def validate(self, attrs):
        if attrs.get('password', False):
            # doğrulama fonksiyonu
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password  # şifreleme fonksiyonu
            password = attrs['password']  # Password al.
            validate_password(password)  # Validation'dan geçir.
            attrs.update(
                {
                    # Password şifrele ve güncelle.
                    'password': make_password(password)
                }
            )
        return super().validate(attrs)  # Orjinal methodu çalıştır.


class UserTokenSerializer(TokenSerializer):
    user = UserSerializer()

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')
