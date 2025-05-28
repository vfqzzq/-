from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'difficulty', 'cooking_time', 'is_published')
    list_filter = ('category', 'difficulty', 'is_published')
    search_fields = ('title', 'ingredients')
