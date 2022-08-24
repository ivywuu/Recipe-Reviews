# Generated by Django 4.1 on 2022-08-24 21:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100)),
                ('pic', models.ImageField(blank=True, default=0, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('tsp', 'tsp'), ('tbsp', 'tbsp'), ('cup', 'cup'), ('g', 'g'), ('mL', 'mL'), ('L', 'L')], default='g', max_length=4)),
                ('amount', models.IntegerField(default=0)),
                ('ingredient', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr', models.CharField(default='', max_length=50)),
                ('temp', models.CharField(blank=True, choices=[('C', 'C'), ('F', 'F')], default='C', max_length=1)),
                ('time', models.DurationField(blank=True, default=datetime.timedelta)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True)),
                ('ingr', models.TextField(blank=True)),
                ('instr', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100)),
                ('pic', models.ImageField(blank=True, default=0, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('review', models.TextField()),
                ('ingr_amount', models.ManyToManyField(to='recipes.ingredientamount')),
                ('tools', models.ManyToManyField(to='recipes.tool')),
            ],
        ),
    ]
