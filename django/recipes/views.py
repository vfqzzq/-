from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

def home(request):
    # Головна сторінка зі списком посилань на інші вюшки
    pages = [
        {'name': 'Page 1', 'url': 'page1'},
        {'name': 'Page 2', 'url': 'page2'},
        {'name': 'Page 3', 'url': 'page3'},
        {'name': 'Page 4', 'url': 'page4'},
        {'name': 'Page 5', 'url': 'page5'},
        {'name': 'Рецепти', 'url': 'recipe_list'},
    ]
    return render(request, 'recipes/home.html', {'pages': pages, 'title': 'Головна сторінка'})

def page1(request):
    return render(request, 'recipes/page.html', {'title': 'Сторінка 1'})

def page2(request):
    return render(request, 'recipes/page.html', {'title': 'Сторінка 2'})

def page3(request):
    return render(request, 'recipes/page.html', {'title': 'Сторінка 3'})

def page4(request):
    return render(request, 'recipes/page.html', {'title': 'Сторінка 4'})

def page5(request):
    return render(request, 'recipes/page.html', {'title': 'Сторінка 5'})

def recipe_list(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('title')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # або на будь-яку сторінку після створення
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})

def soup_recipes(request):
    recipes = Recipe.objects.filter(category__name='Супи', is_published=True)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'title': 'Рецепти: Супи'})

def dessert_recipes(request):
    recipes = Recipe.objects.filter(category__name='Десерти', is_published=True)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'title': 'Рецепти: Десерти'})

def snack_recipes(request):
    recipes = Recipe.objects.filter(category__name='Закуски', is_published=True)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'title': 'Рецепти: Закуски'})

