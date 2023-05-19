from django.db import models

# Create your models here.


class Tutorial(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutorials"
