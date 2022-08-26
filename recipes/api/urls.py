from django.urls import path 
from . import views 

urlpatterns = [
  path('', views.getRoutes),
  path('recipes/', views.getRecipes),
  path('tools/', views.getTools),
  path('ingredient/', views.getIngredients),
  path('ingredientAmount/', views.getIngredientAmount),
  path('instruction/', views.getInstruction),
]
