from django.contrib import admin
from .models import  User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('image_data','nickname','session_key','access_key','password','is_superuser')
    readonly_fields = ('image_data',)


admin.site.register(User, UserAdmin)