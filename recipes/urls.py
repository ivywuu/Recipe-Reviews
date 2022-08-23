from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/', views.recipes, name="recipes"),
    path('pantry/', views.pantry, name="pantry"),
    path('tool', views.tool, name="tool"),

    path('add-rec/',views.addRecipeRec, name="add-rec"),
]
