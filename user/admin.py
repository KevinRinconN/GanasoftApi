from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            ),
        }),
        ('Informacion personal', {
            'fields': (
                'first_name',
                'last_name',
                'email',
            ),
        }),
        ('Permisos', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active',
            ),
        }),
    )
