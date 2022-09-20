from curses import REPORT_MOUSE_POSITION
from rest_framework import serializers
from recipes.models import Recipe,Tool,IngredientAmount,Ingredient,Instruction,IngredientGroup


class ToolSerializer(serializers.ModelSerializer):
  pic = serializers.ImageField(
            max_length=None, use_url=True
        )
  class Meta:
    model = Tool
    fields = ('name','brand','pic')


class IngredientAmountSerialzier(serializers.ModelSerializer):
  ingredient = serializers.StringRelatedField(source='ingredient.name')

  class Meta:
    model = IngredientAmount
    fields = ('ingredient','amount','unit')

class IngredientGroupSerializer(serializers.ModelSerializer):
  rec = serializers.StringRelatedField(source='rec.title')

  ingredientAmounts = IngredientAmountSerialzier(many=True)
  class Meta:
    model = IngredientGroup
    fields = ('name','rec','ingredientAmounts')

class IngredientSerializer(serializers.ModelSerializer):
  pic = serializers.ImageField(
            max_length=None, use_url=True
        )
  class Meta:
    model = Ingredient
    fields = ('name','brand','pic')

class InstructionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Instruction
    fields = ('step','description')


class RecipeSerializer(serializers.ModelSerializer):
  # tools = ToolSerializer(many=True)
  # ingredientAmounts = IngredientAmountSerialzier(many=True)

  ingredientGroups = IngredientGroupSerializer(many=True)
  instructions = InstructionSerializer(many=True)
  pic = serializers.ImageField(
            max_length=None, use_url=True
        )


  class Meta:
    model = Recipe
    fields = ('title','topic','rating','servings','pic','ingredientGroups','instructions','review')

