from rest_framework import generics
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from .serializers import SearchSerializer

from . import client


class SearchListAlgoliaView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get("q")
        tag = request.GET.get("tag")
        public = request.GET.get("public") != "0"

        if query is None:
            return Response({"search_error": "Query not found"}, status=400)
        results = client.perform_search_on_multiple_indices(
            query, "hk_Product, hk_Article", tags=tag, user=user, public=public
        )
        return Response(results)


search_list_algolia = SearchListAlgoliaView.as_view()


class SearchListDjangoView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        q = self.request.GET.get("q")

        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results


search_list_django = SearchListDjangoView.as_view()
