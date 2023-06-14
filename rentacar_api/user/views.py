from .serializers import (
    User, UserSerializer
)

# ------------------------------------
# User Create View
# ------------------------------------

from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

# rest_framework\viewsets.py

'''
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
'''

class UserCreateView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    # rest_framework\mixins.py CreateModelMixin create methodu override ediliyor
    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Permission guvenligi icin override ediliyor
        serializer.validated_data['is_superuser']=False
        serializer.validated_data['is_staff']=False
        serializer.validated_data['is_active']=True
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

# ------------------------------------
# User View
# ------------------------------------

from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet):
    # queryset = User.objects.all()
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    # main\settings.py
    # REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAdminUser'],}
    # permission_classes = [IsAdminUser] # project settings.py => default:IsAdminUser

