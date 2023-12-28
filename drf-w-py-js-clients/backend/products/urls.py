from django.urls import path, re_path
from . import views

urlpatterns = [
    path("<int:pk>/update", views.product_update_view, name="product-edit"),
    path("<int:pk>/delete", views.product_destroy_view),
    path("<int:pk>", views.product_detail_view, name="product-detail"),
    path("list", views.product_mixin_view),
    path("create", views.product_mixin_view),
    path("", views.product_list_create_view, name="product-list-create"),
]
