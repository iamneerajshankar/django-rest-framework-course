from django.contrib import admin
from myApp.models import MoviesLibraryModel


@admin.register(MoviesLibraryModel)
class MoviesLibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'director', 'year', 'rating', 'franchise']
    list_filter = ['name', 'year']
    list_per_page = 50


