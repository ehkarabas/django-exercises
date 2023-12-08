from django.contrib import admin
from .models import Product, Category

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # model ana sayfasinda hangi field'lar gorunecek, tanimnlanan siraya gore konumlandirilir
    list_display = (
        "name",
        "price",
        "isActive",
        "slug",
        "product_categories",
    )
    # <class 'app1.admin.ProductAdmin'>: (admin.E109) The value of 'list_display[4]' must not be a ManyToManyField.
    # hangi field'lara tiklandiginda instance detay sayfasina gidilecek
    list_display_links = ("name", "price")
    # hangi field'lar read only olacak
    # list veya tuple olmasi gerektigi icin tuple ise tek elemanli oldugunda virgul koymayi unutmamak gerekir.
    readonly_fields = ("slug",)
    # prepopulated_fields yalnizca admin panelde gecerlidir
    # prepopulated_fields = {
    #     "slug": ("name",)
    # }  # admin class icinde readonly_fields'tan cikarilmali ve buraya eklenen field'larin option'larinda editable false olmamali
    # editable=False sadece django admin panel instance sayfalarindaki formlarda ilgili field'in goruntulenmemesini saglar.
    # column isimlerine gore filtreleme aktiflestirme
    list_filter = ("categories",)
    # model anasayfasindan field uzerinde edit yapabilmeyi aktiflestirme
    list_editable = (
        "isActive",
    )  # tanimlandiginda liste altinda save(kaydet) butonu belirir
    # model anasayfasinda arama yapildiginda hangi field'lar uzerinde araminin gerceklesecegi
    search_fields = (
        "name",
        "description",
    )  # tanimlandiginda liste uzerinde search bar belirir

    # field value None veya "" oldugunda model anasayfasinda nasil gorunsun"(genel tanim) - default "-"
    empty_value_display = "-empty-"

    # instance detay sayfasi formunda hangi field'lar gorunsun, gruplamali duzen, tanimnlanan siraya gore konumlandirilir, hem fields hem fieldsets tanimlanamaz, biri tercih edilmelidir.
    fieldsets = [
        (
            "Primary options",  # bolume isim vermemek icin
            {
                "classes": ["wide"],  # default wide'tir
                "fields": ["name", "categories", "price"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],  # collapse olursa bolum gizlenir
                "fields": ["description", "image", "slug"],
            },
        ),
    ]

    # field value None veya "" oldugunda model anasayfasinda nasil gorunsun"(field'a ozel tanim)
    @admin.display(empty_value="no desc")
    def view_description(self, obj):
        return obj.description

    # Many-To-Many field'lar list-display ile model anasayfasinda gosterilemiyor. Ancak bu ozel method tanimlanarak asilabilmektedir.
    def product_categories(self, obj):
        product_categories = obj.categories.all()

        return " ".join(
            str(product_category) for product_category in product_categories
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
