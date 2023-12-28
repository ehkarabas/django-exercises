from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = dict()
    if model_data:
        data = model_to_dict(model_data, fields=("id", "title", "price"))

    return JsonResponse(data)


@api_view(["POST"])
def api_home_drf(request, *args, **kwargs):
    form_post_request = request.POST
    drf_post_request = request.data
    serializer = ProductSerializer(data=drf_post_request)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
