from django.contrib import admin
from apps.sightings.models import beephoto

@admin.register(beephoto)
class BeephotoAdmin(admin.ModelAdmin):
    list_display = ["id"]


# Register your models here.
