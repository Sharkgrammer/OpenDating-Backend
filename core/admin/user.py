from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.action(description='Set Inactive')
def set_inactive(self, request, queryset):
    queryset.update(is_active=False)


@admin.action(description='Set Active')
def set_active(self, request, queryset):
    queryset.update(is_active=True)


class UserAdmin(BaseUserAdmin):
    list_display = (
        'id', 'uid', 'email', 'full_name', 'display_name', 'is_active', 'is_admin',
        'is_staff', 'deleted', 'date_joined', 'last_login', 'description'
    )

    fieldsets = (
        ('Personal Info', {'fields': ('uid', 'email', 'full_name', 'display_name', 'description', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff', 'deleted')}),
    )

    add_fieldsets = (
        ("Add User",
         {
             'fields': (
                 'email', 'full_name', 'display_name', 'description', 'password1',
                 'password2'
             )
         }
         )
    )

    list_filter = ('is_active', 'is_admin', 'is_staff', 'deleted')
    search_fields = ('id', 'email', 'full_name', 'display_name')
    ordering = ('-id', 'date_joined', 'last_login')
    actions = [set_inactive, set_active]
