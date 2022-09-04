from rest_framework.decorators import api_view
from rest_framework.response import Response
<<<<<<< HEAD
from recipes.models import Ingredient, Recipe,Tool,IngredientAmount,Instruction
from .serializers import RecipeSerializer,ToolSerializer,IngredientAmountSerialzier,IngredientSerializer,InstructionSerializer
=======
from recipes.models import Ingredient, Recipe,Tool
from .serializers import RecipeSerializer,ToolSerializer
>>>>>>> 179c0b8... api tested
@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /api',
    'GET /api/recipes',
    'GET /api/tools',
<<<<<<< HEAD
    'GET /api/ingredient',
    'GET /api/instruction',
    'GET /api/ingredientAmount',
=======
>>>>>>> 179c0b8... api tested
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
<<<<<<< HEAD
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
=======
>>>>>>> 179c0b8... api tested
  return Response(serializer.data)