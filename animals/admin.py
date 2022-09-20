from django.contrib import admin
from .models import AnimalModel, ShelterModel


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'arrived_at', 'shelter')
    ordering = ('id', 'nickname', 'arrived_at', 'shelter')

class ShelterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(AnimalModel, AnimalAdmin)
admin.site.register(ShelterModel, ShelterAdmin)


