from django.db import models
from django.conf import settings

from django.contrib.auth.models import User as UserModel
from django.db.models.query import QuerySet

from django.db.models import Q

from datetime import datetime


User = settings.AUTH_USER_MODEL


TAGS_MODEL_VALUES = ["electronics", "cars", "boats", "movies", "cameras"]

import random
from typing import List


def get_default_user():
    return UserModel.objects.get_or_create(
        pk=1, defaults={"username": "default", "password": "1234"}
    )[0]


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.none()
        if user is not None:
            qs = self.is_public().filter(lookup, user=user)

        # if user is not None:
        #     qs2 = self.filter(user=user)
        #     qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Product(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        default=1,
        related_name="products",
    )

    title = models.CharField(max_length=120)
    content = models.TextField(null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/products/{self.pk}/"

    def is_public(self) -> bool:
        return self.public

    def get_tags_list(self) -> List[str]:
        return [random.choice(TAGS_MODEL_VALUES)]

    def __str__(self):
        return f"{self.title} / {self.price} - {self.sale_price}"

    @property
    def sale_price(self):
        return f"{(float(self.price) * 0.8):.2f}"

    def get_discount(self):
        return f"{'discount'}"

    @property
    def body(self):
        return self.content
