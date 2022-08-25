from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
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

class Instruction(models.Model):
  class Unit(models.TextChoices):
    Celsius = 'C',_('C')
    Farenheit = 'F', _('F')

  class UnitT(models.TextChoices):
    Day = 'day',_('day')
    Hour = 'hr', _('hr')
    Minute = 'min', _('min')
    Second = 's', _('s')
    OverNight = 'overnight'

  instr = models.CharField(max_length=50,default='')
  temp_num = models.IntegerField(default=0,blank=True)
  temp_unit = models.CharField(max_length=1,choices = Unit.choices, default=Unit.Celsius,blank=True)
  time_num = models.IntegerField(default=0,blank=True)
  time_unit = models.CharField(max_length=10,choices = UnitT.choices, default=UnitT.Minute,blank=True)

  def __str__(self):
    if self.temp_num != 0 and self.time_num != 0:
      return "%s %s %s %s %s" % (self.instr, self.temp_num, self.temp_unit,self.time_num,self.time_unit)
    elif self.temp_num == 0 and self.time_num != 0:
      return "%s %s %s" % (self.instr, self.time_num,self.time_unit)
    elif self.temp_num != 0 and self.time_num == 0:
      return "%s %s %s" % (self.instr, self.temp_num, self.temp_unit)
    return "%s" % (self.instr)


class InstructionIngredient(models.Model):
  instruction = models.ForeignKey(Instruction,on_delete=models.CASCADE,default=NULL)
  ingredient = models.ManyToManyField(IngredientAmount)
  
  def __str__(self):
    ingredients = ", ".join(str(i.ingredient.name) for i in self.ingredient.all())
    return "%s %s" % (self.instruction, ingredients)


class InstructionStep(models.Model):
  step = models.IntegerField(default=1)
  instruction = models.ForeignKey(Instruction,on_delete=models.CASCADE,null=True,blank=True,default=NULL)
  instruct_i = models.ForeignKey(InstructionIngredient,on_delete=models.CASCADE,null=True,blank=True,default=NULL)

  def __str__(self):
    if self.instruction:
      return "Step %s. %s" % (self.step, self.instruction)
    else:
      return "Step %s. %s" % (self.step, self.instruct_i)


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

  





