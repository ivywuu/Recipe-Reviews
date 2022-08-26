from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Tool(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100,blank=True)
  pic = models.ImageField(blank=True,default=NULL)

  def __str__(self):
    return self.name

class Ingredient(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100,blank=True)
  pic = models.ImageField(blank=True,default=NULL)

  def __str__(self):
    return self.name

class Recipe(models.Model):
  tools = models.ManyToManyField(Tool)

  class Topics(models.TextChoices):
    Bread = 'Bread',_('Bread')
    Cake = 'Cake', _('Cake')
    Cookies = 'Cookies', _('Cookies')
    Other = 'Other', _('Other')

  topic = models.CharField(max_length=10,choices = Topics.choices, default=Topics.Other)
  title = models.CharField(max_length=200)
  # link = models.URLField(default=NULL,blank=True,null=True)
  servings = models.IntegerField(default=0,blank=True)
  rating = models.IntegerField(default=0,         validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
  review = models.TextField()

  def __str__(self):
    return self.title


class IngredientAmount(models.Model):

  class Unit(models.TextChoices):
    TEASPOON = 'tsp',_('tsp')
    TABLESPOON = 'tbsp', _('tbsp')
    CUP = 'cup',_('cup')
    GRAM = 'g',_('g')
    MILLILITER = 'mL',_('mL')
    LITER = 'L',_('L')

  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE,default=NULL)
  unit = models.CharField(max_length=4, choices = Unit.choices, default='',blank=True)
  amount = models.IntegerField(default=0,blank=True)
  rec = models.ForeignKey(Recipe,on_delete=models.CASCADE,default=NULL)

  def __str__(self):
    if self.amount !=0 and self.unit !='':
      return "%s : %s%s %s" % (self.rec,self.amount, self.unit, self.ingredient.name)
    elif self.amount !=0 and self.unit =='':
      return "%s : %s %s" % (self.rec, self.amount, self.ingredient.name)
    return "%s : %s" % (self.rec, self.ingredient.name)


class Instruction(models.Model):
  step = models.IntegerField(default=1)
  description = models.TextField()
  rec = models.ForeignKey(Recipe,on_delete=models.CASCADE,default=NULL)

  def __str__(self):
    return "%s : %s. %s" % (self.rec,self.step, self.description)

class RecipeRec(models.Model):
  name = models.CharField(max_length=200,blank=True)
  title = models.CharField(max_length=200)
  link = models.URLField(max_length = 200, blank=True)
  ingr = models.TextField(blank=True)
  instr = models.TextField(blank=True)

  
  def __str__(self):
    return "%s: %s" % (self.name, self.title)

  





