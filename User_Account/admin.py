from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'role',
                    'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser',)
    search_fields = ('first_name', 'last_name', 'username', 'email', 'role',)
    list_filter = ('first_name', 'last_name', 'username', 'email', 'role',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    fieldsets = ()


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user', 'country', 'city']
