from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    image = models.URLField(blank=True)
    bio = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
 
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

User.add_to_class('image', models.URLField(max_length = 400, default='https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png'))
User.add_to_class('bio', models.TextField(blank=True, null=True, max_length = 1500))

 