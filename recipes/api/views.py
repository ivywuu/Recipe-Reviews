from rest_framework.decorators import api_view
from rest_framework.response import Response
from recipes.models import Ingredient, Recipe,Tool,IngredientAmount,Instruction,IngredientGroup
from .serializers import RecipeSerializer,ToolSerializer,IngredientAmountSerialzier,IngredientSerializer,InstructionSerializer
from recipes.models import Ingredient, Recipe,Tool
from .serializers import RecipeSerializer,ToolSerializer,IngredientGroupSerializer

@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /api',
    'GET /api/recipes',
    'GET /api/tools',
    'GET /api/ingredient',
    'GET /api/instruction',
    'GET /api/ingredientAmount',
    'GET /api/ingredientGroup',
  ]

  return Response(routes)

@api_view(['GET'])
def getIngredientGroup(request):
  groups = IngredientGroup.objects.all()
  serializer = IngredientGroupSerializer(groups,many=True)
  return Response(serializer.data)

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

@api_view(['GET'])
def getIngredients(request):
  ingredient = Ingredient.objects.all()
  serializer = IngredientSerializer(ingredient,many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getIngredientAmount(request):
  ingredientAmount = IngredientAmount.objects.all()
  serializer = IngredientAmountSerialzier(ingredientAmount,many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getInstruction(request):
  instruction = Instruction.objects.all()
  serializer = InstructionSerializer(instruction,many=True)
  return Response(serializer.data)