from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_superuser', 'is_staff')
    list_editable = ('email', 'is_active',)
    ordering = ('username', )
