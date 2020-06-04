from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Profile

admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fk_name = 'user'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

