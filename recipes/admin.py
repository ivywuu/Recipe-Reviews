from django.contrib import admin

# Register your models here.

from .models import Tool,Ingredient,RecipeRec,Recipe,IngredientAmount,Instruction,IngredientGroup


admin.site.register(Tool)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(IngredientGroup)
admin.site.register(IngredientAmount)
admin.site.register(Instruction)
admin.site.register(RecipeRec)
