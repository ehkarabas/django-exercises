from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Purchase,
    Sale,
)
# admin.site.register(Category)
# admin.site.register(Brand)
# admin.site.register(Product)
# admin.site.register(Firm)
# admin.site.register(Purchase)
# admin.site.register(Sale)

# --------------------------------------------
# Hızlı işlem menüsündeki silme işleminin stok ekle/çıkar yapması için:
from django.contrib.admin.options import ModelAdmin
class CustomModelAdmin(ModelAdmin):
    # Override:
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
# --------------------------------------------
admin.site.register(Category, CustomModelAdmin)
admin.site.register(Brand, CustomModelAdmin)
admin.site.register(Product, CustomModelAdmin)
admin.site.register(Firm, CustomModelAdmin)
admin.site.register(Purchase, CustomModelAdmin)
admin.site.register(Sale, CustomModelAdmin)