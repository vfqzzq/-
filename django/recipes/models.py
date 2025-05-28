from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Назва категорії
    description = models.TextField(blank=True)            # Опис категорії (не обов'язково)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)              # Назва рецепту
    description = models.TextField(blank=True)             # Опис рецепту
    ingredients = models.TextField()                        # Інгредієнти (обов'язково)
    instructions = models.TextField()                       # Інструкції (обов'язково)
    cooking_time = models.PositiveIntegerField(default=30) # Час приготування (хвилини, дефолт 30)
    difficulty = models.PositiveSmallIntegerField(default=1, choices=[(1,'Easy'), (2,'Medium'), (3,'Hard')])  # Складність
    is_published = models.BooleanField(default=True)       # Опубліковано (дефолт True)
    created_at = models.DateTimeField(auto_now_add=True)   # Дата створення (автоматично)
    updated_at = models.DateTimeField(auto_now=True)       # Дата оновлення (автоматично)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')  # Категорія рецепту

    def __str__(self):
        return self.title
