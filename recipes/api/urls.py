from django.urls import path 
from . import views 

urlpatterns = [
  path('', views.getRoutes),
  path('recipes/', views.getRecipes),
  path('tools/', views.getTools),
<<<<<<< HEAD
  path('ingredient/', views.getIngredients),
  path('ingredientAmount/', views.getIngredientAmount),
  path('instruction/', views.getInstruction),
=======
>>>>>>> 179c0b8... api tested
]
