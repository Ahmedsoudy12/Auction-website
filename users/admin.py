from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add the custom fields to the list display
    list_display = ('username', 'email', 'gender', 'notify_me', 'is_staff', 'is_active')
    # Add the custom fields to the fieldsets for editing
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'notify_me')}),
    )
    # Add the custom fields to the add_fieldsets for creating new users
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('gender', 'notify_me')}),
    )

# Register the custom user model with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)