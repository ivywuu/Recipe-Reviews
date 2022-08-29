from curses import REPORT_MOUSE_POSITION
from rest_framework.serializers import ModelSerializer
from recipes.models import Recipe,Tool

class ToolSerializer(ModelSerializer):
  class Meta:
    model = Tool
    fields = '__all__'

class RecipeSerializer(ModelSerializer):
  tools = ToolSerializer(many=True)
  class Meta:
    model = Recipe
    fields = ('tools','title','topic')
