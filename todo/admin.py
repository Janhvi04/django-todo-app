from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from todo.models import TODOO


# Note: User model is automatically registered by Django when django.contrib.auth is in INSTALLED_APPS
# No need to register it explicitly - it's already available in admin panel


@admin.register(TODOO)
class TODOOAdmin(admin.ModelAdmin):
    list_display = ('srno', 'title', 'user', 'completed', 'data')
    list_filter = ('completed', 'data', 'user')
    search_fields = ('title', 'user__username')
    readonly_fields = ('srno', 'data')
    ordering = ('-data',)
    
    fieldsets = (
        ('Todo Information', {
            'fields': ('srno', 'title', 'user', 'completed', 'data')
        }),
    )