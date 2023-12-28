from django.contrib import admin


from .models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "content",
        "public",
        "user",
    )

    ordering = ["pk", "user", "public"]

    list_editable = ("public",)

    list_display_links = ("pk", "title")
    readonly_fields = ("pk",)

    fields = (
        "pk",
        "user",
        "title",
        "content",
        "price",
        "public",
    )
