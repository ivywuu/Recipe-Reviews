from django.forms import ModelForm
from .models import Tool,Ingredient,RecipeRec


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

    
    