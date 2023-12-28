from rest_framework import serializers
from products.models import Product
from django.contrib.auth import get_user_model
from api.serializers import UserPublicSerializer

User = get_user_model()


class SearchSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-edit", lookup_field="pk", read_only=True
    )
    owner = serializers.SerializerMethodField()
    title = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)
    public = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "pk",
            "url",
            "owner",
            "title",
            "content",
            "public",
        )

    def get_owner(self, obj):
        user_serializer = UserPublicSerializer(
            obj.user,
            context={
                **self.context,
                "exclude_product_id": obj.id,
            },
        )
        return user_serializer.data
