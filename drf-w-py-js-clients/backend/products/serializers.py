from rest_framework import serializers
from .models import Product

from django.urls import reverse as django_reverse

from rest_framework.reverse import reverse as drf_reverse

from . import validators

from api.serializers import UserPublicSerializer

from django.conf import settings

from django.contrib.auth import get_user_model


User = get_user_model()


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-edit", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-edit", lookup_field="pk"
    )
    title = serializers.CharField(
        max_length=120,
        validators=[
            validators.validate_title_no_title,
            validators.unique_product_title,
        ],
    )
    owner = serializers.SerializerMethodField()
    body = serializers.CharField(source="content")

    class Meta:
        model = Product

        fields = [
            "pk",
            "url",
            "owner",
            "title",
            "body",
            "price",
            "sale_price",
            "public",
            "path",
            "endpoint",
        ]

    def create(self, validated_data):
        obj = super().create(validated_data)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.pop("email") if validated_data.get("email") else None
        if validated_data.get("content") is None:
            instance.content = validated_data.get("title")

        content = validated_data.pop("content")

        return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get("request")

        if request is None:
            return django_reverse("product-edit", kwargs={"pk": obj.pk})

        return drf_reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, "id") or not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def get_my_user_data(self, obj):
        return {"username": obj.user.username}

    def get_owner(self, obj):
        user_serializer = UserPublicSerializer(
            obj.user,
            context={
                **self.context,
                "exclude_product_id": obj.id,
            },
        )
        return user_serializer.data
