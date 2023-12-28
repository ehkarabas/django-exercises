from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-edit", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        exclude_product_id = self.context.get("exclude_product_id")
        user = obj
        my_products_qs = user.products.exclude(id=exclude_product_id)[:5]
        return UserProductInlineSerializer(
            my_products_qs, many=True, context=self.context
        ).data
