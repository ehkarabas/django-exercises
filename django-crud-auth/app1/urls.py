from django.urls import path

# from . import views
from .views import (
    index,
    create,
    edit,
    delete,
    list_products_by_query,
    upload,
    getProductsByProductNameSlug,
)

urlpatterns = [
    path("", index, name="product_index"),
    path("edit/<int:id>", edit, name="edit_product"),
    path("delete/<int:id>", delete, name="delete_product"),
    path("create", create, name="create_product"),
    path("list", list_products_by_query, name="list_products_by_query"),
    path("upload", upload, name="upload_image"),
    path(
        "<slug:product_name_slug>",
        getProductsByProductNameSlug,
        name="products_by_slug",
    ),
]
