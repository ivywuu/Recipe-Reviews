from django.shortcuts import render,redirect
from .models import Recipe, Tool,Ingredient,RecipeRec,IngredientAmount,Instruction,IngredientGroup
from django.contrib.auth.decorators import login_required
from .forms import RecipeRecForm,RecipeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import re
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

@login_required(login_url='/login')
def addRecipe(request):
  form = RecipeForm()
  if request.method == 'POST':
    form = RecipeForm(request.POST)

    if form.is_valid():
      rec = form.save(commit=False)
      rec.save()
      ingr_list = request.POST.get('ingredient_list')
      ingr_list = ingr_list.split("\n")
      ingr_list = list(filter(None, (i.rstrip() for i in ingr_list)))


      new_sub = ''
      empty_sub = ''
      sub_categories = False

      for i in ingr_list:
        if i not in ['\n', '\r\n'] :
          if i.isalpha():
            new_sub = IngredientGroup.objects.create(rec=rec)
            new_sub.name = i
            sub_categories = True
          else:
            i_list = i.split(' ',1)
            amount = 0
            unit = '' 
            res = re.split('(\d+)', i_list[0])
            res.remove(res[0])
            i_list.remove(i_list[0])
            i_list = res + i_list

            amount = i_list[0]
            unit = i_list[1]
            ingr = i_list[2]

            new_i_amount = ''

            if sub_categories is False and empty_sub == '':
              empty_sub = IngredientGroup.objects.create(rec=rec)

            if Ingredient.objects.filter(name = ingr).exists():
              found_i = Ingredient.objects.get(name = ingr)
              if sub_categories is True:
                new_i_amount = IngredientAmount.objects.create(ingredient = found_i, group= new_sub)
              else:
                new_i_amount = IngredientAmount.objects.create(ingredient = found_i, group= empty_sub)      
            else:
              new_i = Ingredient.objects.create()
              new_i.name = ingr
              new_i.save()
              if sub_categories is True:
                new_i_amount = IngredientAmount.objects.create(ingredient = new_i, group= new_sub)
              else:
                new_i_amount = IngredientAmount.objects.create(ingredient = found_i, group= empty_sub)          
            new_i_amount.amount = amount
            new_i_amount.unit = unit
            new_i_amount.save()
            if sub_categories is True:
              new_sub.save()
            else:
              empty_sub.save()
        
      #separate instructions 
      inst_list = request.POST.get('instruction_list')
      inst_list = inst_list.split("\n")
      inst_list = list(filter(None, (i.rstrip() for i in inst_list)))

      step = 1 

      for i in inst_list:
        i_list = i.split(' ',1)  

        new_inst = Instruction.objects.create(rec=rec) 
        new_inst.step = step 
        new_inst.description = i_list[1] 
        step += 1
        new_inst.save()


      return redirect('home') 
  
  context = {'form':form}
  return render(request,'recipes/addRecipe.html',context)

