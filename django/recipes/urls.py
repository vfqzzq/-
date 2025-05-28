from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                  # Головна сторінка зі списком посилань
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('page5/', views.page5, name='page5'),
    path('recipes/', views.recipe_list, name='recipe_list'),          # Сторінка з рецептами
    path('recipes/create/', views.create_recipe, name='create_recipe'), # Створення рецепту
    path('recipes/soups/', views.soup_recipes, name='soup_recipes'),
    path('recipes/desserts/', views.dessert_recipes, name='dessert_recipes'),
    path('recipes/snacks/', views.snack_recipes, name='snack_recipes'),
]
