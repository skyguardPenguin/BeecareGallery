from django.contrib import admin
from apps.sightings.models import species, sightings,beephoto
@admin.register(species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(sightings)
class SightingsAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(beephoto)
class BeephotoAdmin(admin.ModelAdmin):
    list_display = ["id"]


# Register your models here.
