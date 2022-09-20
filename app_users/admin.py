from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'shelter')
    ordering = ('user', 'shelter')

admin.site.register(Profile, ProfileAdmin)