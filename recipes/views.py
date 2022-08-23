from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tool,Ingredient,RecipeRec
from .forms import RecipeRecForm

# Create your views here.
def home(request):
  return render(request,'recipes/home.html')

def recipes(request):
  return render(request,'recipes/recipes.html')

def pantry(request):
  return render(request,'recipes/pantry.html')

def tool(request):
  tools = Tool.objects.all()
  context = {'tools':tools}
  return render(request,'recipes/tools.html',context)

def addRecipeRec(request):
  form = RecipeRecForm()
  if request.method == 'POST':
    form = RecipeRecForm(request.POST)
    if form.is_valid():
      rec = form.save(commit=False)
      rec.save()
      return redirect('home')
  context = {'form':form}
  return render(request,'recipes/recForm.html',context)




