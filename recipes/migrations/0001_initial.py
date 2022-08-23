# Generated by Django 4.1 on 2022-08-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingr_name', models.CharField(max_length=100)),
                ('ingr_brand', models.CharField(max_length=100)),
                ('ingr_pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('tsp', 'teaspoon'), ('tbsp', 'tablespoon'), ('cup', 'cup'), ('g', 'gram'), ('mL', 'milliliter'), ('L', 'Liter')], default='g', max_length=4)),
                ('amount', models.IntegerField(default=0)),
                ('ingredient', models.ManyToManyField(to='recipes.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=100)),
                ('tool_brand', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('rec_title', models.CharField(max_length=200)),
                ('rec_review', models.TextField()),
                ('ingr_amount', models.ManyToManyField(to='recipes.ingredientamount')),
                ('tools', models.ManyToManyField(to='recipes.tool')),
            ],
        ),
    ]
