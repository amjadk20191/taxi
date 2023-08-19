from django.contrib import admin

from .models import User ,problem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'phone',
        'is_active',
        'is_staff',
        'group',
    )
    list_filter = ('last_login', 'is_superuser', 'is_active', 'is_staff')
    raw_id_fields = ('groups', 'user_permissions')
    
    
    
@admin.register(problem)
class proplemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description')
    list_filter = ('user',)