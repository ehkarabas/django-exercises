from .serializers import (
    User, UserSerializer
)

# --------------------------------------------------------
# UserCreateView -> Only CreateUser for permissions.AllowAny
# --------------------------------------------------------
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

class UserCreateView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # # Permission guvenligi icin override ediliyor. Defaults:
        serializer.validated_data['is_superuser'] = False
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_active'] = True
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# --------------------------------------------------------
# UserView -> Full Control for permissions.IsAdminUser
# --------------------------------------------------------
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
# Django REST Framework'da DefaultRouter veya SimpleRouter kullanıldığında, her bir viewset için otomatik olarak belirli URL'ler oluşturulur. Bu URL'ler, belirtilen basename'e ve belirli bir kalıba bağlıdır.
"""
Her bir viewset için oluşturulan URL'ler şu şekildedir:

<basename>-list: Viewset'in list() metodu için. Bu, genellikle bir HTTP GET isteği ile erişilen ve tüm kaynakları listeler.
<basename>-detail: Viewset'in retrieve() metodu için. Bu, belirli bir kaynağı almak için kullanılır.
<basename>-create: Viewset'in create() metodu için. Bu, yeni bir kaynak oluşturmak için kullanılır.
<basename>-update ve <basename>-partial-update: Viewset'in update() metodu için. Bu, bir kaynağı güncellemek için kullanılır.
<basename>-destroy: Viewset'in destroy() metodu için. Bu, bir kaynağı silmek için kullanılır.

Bu URL'ler basename ile birleştirilerek belirlenir. Örneğin, router.register('users', UserViewSet, basename='user') ifadesi şu URL'leri oluşturur:

user-list: Tüm kullanıcıları listelemek için.
user-detail: Belirli bir kullanıcıyı almak için.
user-create: Yeni bir kullanıcı oluşturmak için.
user-update ve user-partial-update: Bir kullanıcıyı güncellemek için.
user-destroy: Bir kullanıcıyı silmek için.
"""

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('create-user-list', request=request, format=format),
        # 'list': reverse('user-list', request=request, format=format), # post yalnizca register'a olmali(token olusturmasi ve create disinda diger tum user detaylarinin staff uzeri permissionda olmasi icin)
        'list': {
            'url': reverse('user-list', request=request, format=format),
            'methods': {
                'GET': 'Retrieve a list of users',
                'PUT': 'Update a user',
                'POST': 'Create a new user',
                'PATCH': 'Partially update a user',
                'DELETE': 'Delete a user',
            },
            'permission' : 'Admin users only',
        },
        # 'auth': reverse('rest_login', request=request, format=format),
        'auth': request.build_absolute_uri('/account/auth/'), # sabit bir URL'yi döndürmek istiyorsanız, tam URL'yi elle oluşturabilirsiniz
    })


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'api-root': reverse('api_root', request=request, format=format),
#         'register': {
#             'url': reverse('user-register', request=request, format=format),
#             'method': 'POST'
#         },
#         'list-users': {
#             'url': reverse('user-list', request=request, format=format),
#             'method': 'GET'
#         },
#         'create-user': {
#             'url': reverse('user-create', request=request, format=format),
#             'method': 'POST'
#         },
#         'update-user': {
#             'url': reverse('user-update', args=[1], request=request, format=format),  # Example for id=1
#             'method': 'PUT'
#         },
#         'partial-update-user': {
#             'url': reverse('user-partial-update', args=[1], request=request, format=format),  # Example for id=1
#             'method': 'PATCH'
#         },
#         'destroy-user': {
#             'url': reverse('user-destroy', args=[1], request=request, format=format),  # Example for id=1
#             'method': 'DELETE'
#         },
#         'auth': {
#             'url': reverse('rest_login', request=request, format=format),
#             'method': 'POST'
#         },
#     })

# "update-user", "partial-update-user" ve "destroy-user" gibi işlemleri tek bir URL'de toplamak istenirse	(ModelViewSet detail endpoint'i gibi), GenericAPIView kullanilarak bu islem gerceklestirilebilir.		

"""
from rest_framework.generics import GenericAPIView

class UserDetailView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

urls.py:
from django.urls import path

urlpatterns = [
    # Diğer URL'ler...
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # Diğer URL'ler...
]
"""