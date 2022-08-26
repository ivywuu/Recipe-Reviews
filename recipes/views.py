from django.shortcuts import render,redirect
from .models import Tool,Ingredient,RecipeRec
from django.contrib.auth.decorators import login_required
from .forms import RecipeRecForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def loginPage(request):
  page = 'login'

  if request.user.is_authenticated:
    return redirect('home')

  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')

    try: 
      user = User.objects.get(username=username) 
    except:
      messages.error(request, 'User does not exist')
    
    user = authenticate(request,username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      messages.error(request, 'Username OR password does not exist')

  context = {'page':page}
  return render(request,'recipes/login_register.html',context)

def logoutUser(request):
  logout(request)
  return redirect('home')

def home(request):
  return render(request,'recipes/home.html')

def recipes(request):
  return render(request,'recipes/recipes.html')

def pantry(request):
  pantry = Ingredient.objects.all()
  context = {'pantry':pantry}
  return render(request,'recipes/pantry.html',context)

def tool(request):
  tools = Tool.objects.all()
  context = {'tools':tools}
  return render(request,'recipes/tools.html',context)

@login_required(login_url='login')
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




