# En tu archivo admin.py
from django.contrib import admin
from .models import Location
from .models import Category

admin.site.register(Category)
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'description','category')


