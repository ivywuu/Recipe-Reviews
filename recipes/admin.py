from django.contrib import admin

# Register your models here.

from .models import Tool,Ingredient,IngredientAmount,Recipe,RecipeRec

admin.site.register(Tool)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
admin.site.register(Recipe)
admin.site.register(RecipeRec)
