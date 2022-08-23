from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as _

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

class IngredientAmount(models.Model):

  class Unit(models.TextChoices):
    TEASPOON = 'tsp',_('tsp')
    TABLESPOON = 'tbsp', _('tbsp')
    CUP = 'cup',_('cup')
    GRAM = 'g',_('g')
    MILLILITER = 'mL',_('mL')
    LITER = 'L',_('L')

  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE,default=NULL)
  unit = models.CharField(max_length=4, choices = Unit.choices, default=Unit.GRAM)
  amount = models.IntegerField(default=0)

  def __str__(self):
    return "%s%s %s" % (self.amount, self.unit, self.ingredient.name)

  
class Recipe(models.Model):
  ingr_amount = models.ManyToManyField(IngredientAmount)
  tools = models.ManyToManyField(Tool)

  rating = models.IntegerField(default=0)
  title = models.CharField(max_length=200)
  review = models.TextField()

  def __str__(self):
    return self.title

class RecipeRec(models.Model):
  name = models.CharField(max_length=200,blank=True)
  title = models.CharField(max_length=200)
  link = models.URLField(max_length = 200, blank=True)
  ingr = models.TextField(blank=True)
  instr = models.TextField(blank=True)

  
  def __str__(self):
    return "%s: %s" % (self.name, self.title)

  





