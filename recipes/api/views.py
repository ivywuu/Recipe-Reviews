from rest_framework.decorators import api_view
from rest_framework.response import Response
from recipes.models import Ingredient, Recipe,Tool
from .serializers import RecipeSerializer,ToolSerializer
@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /api',
    'GET /api/recipes',
    'GET /api/tools',
  ]

  return Response(routes)

@api_view(['GET'])
def getRecipes(request):
  recipes = Recipe.objects.all()
  serializer = RecipeSerializer(recipes,many=True)
  return Response(serializer.data)


@api_view(['GET'])
def getTools(request):
  tools = Tool.objects.all()
  serializer = ToolSerializer(tools,many=True)
  return Response(serializer.data)