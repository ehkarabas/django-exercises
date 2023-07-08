from django.contrib import admin

from .models import UserProfile
admin.site.register(UserProfile)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('image', 'bio',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)