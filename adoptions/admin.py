from django.contrib import admin

from .models import Pet
from .models import Vaccination

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "species", "breed", "age", "sex"]

@admin.register(Vaccination)
class VaccineAdmin(admin.ModelAdmin):
    pass