from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['username', 'email', 'is_admin']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None,{'fields' :('is_admin')})
    )
    list_filter = ['username', 'email', 'is_admin']
    search_fields = ['username']
    
admin.site.register(User, UserAdmin)