# Generated by Django 4.1 on 2022-08-26 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('Bread', 'Bread'), ('Cake', 'Cake'), ('Cookies', 'Cookies'), ('Other', 'Other')], default='Other', max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField(default=0)),
                ('servings', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('review', models.TextField()),
                ('tools', models.ManyToManyField(to='recipes.tool')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=True, choices=[('tsp', 'tsp'), ('tbsp', 'tbsp'), ('cup', 'cup'), ('g', 'g'), ('mL', 'mL'), ('L', 'L')], default='', max_length=4)),
                ('amount', models.IntegerField(blank=True, default=0)),
                ('ingredient', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
            ],
        ),
    ]
