from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('is_applicant',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff','is_employer','is_comforter', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # list_display_links = ('email',)
    list_display = ('email', 'is_staff','is_applicant', 'is_employer','is_comforter')
    search_fields = ('email', 'is_applicant','is_employer')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)