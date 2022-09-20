from pyexpat import model
from django.forms import ModelForm
from .models import Tool,Ingredient,RecipeRec,Recipe
from django import forms

class RecipeRecForm(ModelForm):
  class Meta:
    model = RecipeRec
    fields = '__all__'


class ToolForm(ModelForm):
  class Meta:
    model = Tool
    fields = '__all__'

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient
    fields = '__all__'

class RecipeForm(ModelForm):
  class Meta:
    model = Recipe
    fields = '__all__'
    
    