from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image', 'bio']

class RegisterSerializer(serializers.ModelSerializer):
 
    id = serializers.IntegerField(read_only=True)
 
    email = serializers.EmailField(
        required = True,
        validators = [
            UniqueValidator(queryset=User.objects.all())
        ],
    )

    password = serializers.CharField(
        write_only = True,   
        required = True,
        validators = [
            validate_password
        ],
        style = {
            'input_type':'password',
        }
    )
 
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {
            'input_type':'password',
        }
    )

    first_name = serializers.CharField(
        max_length = 150,
    )

    last_name = serializers.CharField(
        max_length = 150,
    )

    image = serializers.URLField(
        max_length = 400,
    )

    bio = serializers.CharField(
        required = False,
        allow_blank = True,
        max_length = 1500,
    )

    class Meta:
        model = User
        fields = (
            "id",
            'username',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'image',
            'bio',
        )
 
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
 
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
 
        UserProfile.objects.create(user=user, image=user.image, bio=user.bio)
 
        return user

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            data = {
                "password": "Password fields does not match!!!"
            }
            raise serializers.ValidationError(data)
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
              "last_login",
              "date_joined",
              "groups",
              "user_permissions",
          ]
 
    def get_fields(self, *args, **kwargs):
          fields = super().get_fields(*args, **kwargs)
          request = self.context.get('request', None)
          if request and getattr(request, 'method', None) == "PUT":
              fields['password'].required = False
          return fields
 
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
 
    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password

            password = attrs['password']
            validate_password(password)
            attrs.update({'password': make_password(password)})
 
        return super().validate(attrs)
 
class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user',
        )