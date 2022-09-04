from curses import REPORT_MOUSE_POSITION
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from recipes.models import Recipe,Tool,IngredientAmount,Ingredient

class ToolSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tool
    fields = '__all__'


class IngredientAmountSerialzier(serializers.ModelSerializer):
  ingredient = serializers.StringRelatedField(source='ingredient.name')

  class Meta:
    model = IngredientAmount
    fields = ('ingredient','amount','unit')

class IngredientSerializer(ModelSerializer):
  ingredientAmounts = IngredientAmountSerialzier(many=True)
  class Meta:
    model = Ingredient
    fields = ('name','brand','ingredientAmounts')

class RecipeSerializer(serializers.ModelSerializer):
  tools = ToolSerializer(many=True)
  ingredientAmounts = IngredientAmountSerialzier(many=True)
  class Meta:
    model = Recipe
    fields = ('title','topic','rating','servings','ingredientAmounts','review','tools')
