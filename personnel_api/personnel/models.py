from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class FixModel(models.Model):
    created_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(FixModel):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Departman'
        verbose_name_plural = 'Departmanlar'

    def __str__(self):
        return self.name

class Personnel(FixModel):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('0', 'Not Prefer To Say'),
    )

    TITLES = (
        ('S', 'Senior'),
        ('M','Mid Level'),
        ('J','Junior')
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDERS, default='0')
    title = models.CharField(max_length=1, choices=TITLES, default='J')
    salary = models.PositiveIntegerField()
    started_date = models.DateField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='personnels')

    class Meta:
        verbose_name = 'Personel'
        verbose_name_plural = 'Personeller'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"