from rest_framework import generics, mixins, permissions, authentication

from .models import Product
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import Http404
from django.shortcuts import get_object_or_404

from django.urls import reverse

from api.mixins import StaffEditorPermissionMixin, UserQuerysetMixin

from django.conf import settings
from django.contrib.auth.models import User as UserModel

User = settings.AUTH_USER_MODEL


class DispatchMixin:
    def dispatch(self, request, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"==>> {class_name} args: {args}")
        print(f"==>> {class_name} kwargs: {kwargs}")
        print(f"==>> {class_name} request: {request}")
        print(f"==>> {class_name} dir(request): {dir(request)}")
        print(f"==>> {class_name} request.headers: {request.headers}")
        print(f"==>> {class_name} reqeust.contet_type: {request.content_type}")
        print(f"==>> {class_name} request.body: {request.body}")
        return super().dispatch(request, *args, **kwargs)


class ProductDetailAPIView(
    DispatchMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductCreateAPIView(
    DispatchMixin, StaffEditorPermissionMixin, generics.CreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content", None)
        if content is None:
            content = serializer.validated_data.get("title")

        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()


class ProductListAPIView(
    DispatchMixin, StaffEditorPermissionMixin, generics.ListAPIView
):
    """
    Kullanilmayacak
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


class ProductListCreateAPIView(
    DispatchMixin,
    StaffEditorPermissionMixin,
    UserQuerysetMixin,
    generics.ListCreateAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        email = (
            serializer.validated_data.pop("email")
            if serializer.validated_data.get("email")
            else None
        )
        content = serializer.validated_data.get("content", None)
        if content is None:
            content = serializer.validated_data.get("title")

        serializer.save(user=self.request.user, content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        qs = Product.objects.all()
        list_data = ProductSerializer(qs, many=True).data
        return Response(list_data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            content = serializer.validated_data.get("content", None)
            if content is None:
                content = serializer.validated_data.get("title")

            serializer.save(content=content)
            return Response(serializer.data)


class ProductUpdateAPIView(
    DispatchMixin, StaffEditorPermissionMixin, generics.UpdateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        return super().perform_update(serializer)


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    DispatchMixin, StaffEditorPermissionMixin, generics.DestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


class ProductMixinView(
    DispatchMixin,
    StaffEditorPermissionMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):  # HTTP -> get
        pk = kwargs.get("pk", None)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # HTTP -> post
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content", None)
        if content is None:
            content = "this is a single view doing cool stuff"

        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()
