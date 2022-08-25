from django.contrib import admin

# Register your models here.

from .models import Tool,Ingredient,IngredientAmount,Recipe,RecipeRec,Instruction,InstructionIngredient,InstructionStep,simpleInstruction

admin.site.register(Tool)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
admin.site.register(simpleInstruction)
admin.site.register(Instruction)
admin.site.register(InstructionIngredient)
admin.site.register(InstructionStep)
admin.site.register(Recipe)
admin.site.register(RecipeRec)
