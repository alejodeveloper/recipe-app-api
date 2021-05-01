"""
app.recipe_users.admin
----------------------
Admin for Recipe users models
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from . import models


class UserAdmin(BaseUserAdmin):
    # How the list User Admin page gonna show the data
    ordering = ['id']
    list_display = ['name', 'email']
    # Fields of the single User admin page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser',)
            }
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )

    # Fields of the add admin User page
    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': ('email', 'password1','password2',),
         }),
    )


admin.site.register(models.User, UserAdmin)
