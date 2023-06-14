from django.db import models

# Create your models here.

# ------------------------------------
# Fix Model
# ------------------------------------

from django.contrib.auth.models import User

class FixModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Bir table olarak algilanmaz, diger modeller icin yazilmis bir model oldugu algilanir.
    class Meta:
        abstract = True

# ------------------------------------
# Car Model
# ------------------------------------

from django.core.validators import MinValueValidator

class Car(FixModel):
    GEAR = (
        (1, "Auto"),
        (0, "Manual"),
    )

    plate = models.CharField(max_length=16,unique=True)
    brand = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    year = models.PositiveSmallIntegerField()
    gear = models.BooleanField(choices=GEAR, default=0)
    rent_per_day = models.DecimalField(
        max_digits=8, # noktadan once 4 karakter olmak uzere toplam 6 karakter
        decimal_places=2, # noktadan sonra 2 karakter
        validators=[MinValueValidator(1)] # django.core.validators sayesinde min deger belirleme
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model} # {self.plate}"
    

# ------------------------------------
# Reservation Model
# ------------------------------------
class Reservation(FixModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"[{self.user}] - {self.car} - {self.start_date} - {self.end_date}"
    
    # Django Rest Framework (DRF) ve Django Admin'in farklı yaklaşımlarla çalıştığını bilmek önemlidir. Django'daki UniqueConstraintlar genellikle veritabanı seviyesinde bir kısıtlamadır ve bu, bir save() işlemi sırasında yürütülür. Ancak, bu tür bir kısıtlama, DRF serializer'ı tarafından kontrol edilmez.
    # Yani asagidaki Meta class'i ile Django Admin panel'de yeni Reservation olusturulurken beklenen hata doner ancak DRF Template'te(browser) donmez, hata alinmadan POST gerceklesir. Bunun nedeni DRF'nin de ayni benzersizligi tanimasi icin serializer'da da validate yapilmasi gerekliligidir.
    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/models/constraints/
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'start_date', 'end_date'], name='user_rent_date'
            )
        ]
        # Birden fazla field'i belirli bir duruma gore(bu ornek icin ayni user kapsaminda) unique yapmak icin model meta'sinda constraints kullanilmalidir.
        # Ayni tarihlerde ayni kullanici birden fazla reservation olusturamiyor.
        # Please correct the error below.
        # Reservation with this User, Start date and End date already exists.