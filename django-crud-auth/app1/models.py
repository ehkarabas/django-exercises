from django.db import models
from django.utils.text import slugify
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)


class Category(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.name}"

    def to_dict(self):
        return {
            "name": self.name,
        }

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Address(models.Model):
    street = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    postal_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)])
    city = models.CharField(max_length=30, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.city} - {self.postal_code}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def to_dict(self):
        return {
            "street": self.street,
            "postal_code": self.postal_code,
            "city": self.city,
        }


class Supplier(models.Model):
    company_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name="supplier", null=True
    )

    def __str__(self):
        return f"{self.company_name}"

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def to_dict(self):
        return {
            "company_name": self.company_name,
            "address": self.address.to_dict() if self.address else None,
        }


class Product(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(99999.99)],
    )  # tam kismi 5 ondalik kismi 2 basamakli sayi
    description = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    image = models.FileField(
        upload_to="images", default=None
    )  # MEDIA_ROOT = "uploads" => file path -> "uploads/images"
    isActive = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name="products")

    # editable=False sadece django admin panel instance sayfalarindaki formlarda ilgili field'in goruntulenmemesini saglar.
    slug = models.SlugField(blank=True, unique=True, editable=False)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="products"
    )

    class Meta:
        indexes = [
            models.Index(fields=["slug"], name="slug_index"),
        ]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        self.slug = slugify(
            self.name
        )  # slug field'a gore slugify function'iyla slug field degeri uretme
        super(Product, self).save(*args, **kwargs)  # default model save islevi

    def __str__(self):
        return f"{self.name} - {self.price}"

    # product'i json haline getirmek icin ve ayni modeli kullanan baska bir projeye database verilerini tasimak icin
    def to_dict(self):
        return {
            "name": self.name,
            "price": float(
                self.price
            ),  # JSON modülünün Python'un Decimal tipini doğrudan desteklemedigi icin
            "description": self.description,
            "imageUrl": self.imageUrl,
            "isActive": self.isActive,
            "categories": [
                category.name for category in self.categories.all()
            ],  # Kategorilerin isimlerini liste halinde döndür
            "supplier": self.supplier.company_name,  # ForeignKey field'inda degere erismek gerekir,
        }


class UploadModel(models.Model):
    image = models.FileField(upload_to="images")

    def __str__(self):
        return f"{self.image}"
