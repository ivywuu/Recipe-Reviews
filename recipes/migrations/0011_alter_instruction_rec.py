# Generated by Django 4.1 on 2022-09-04 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_ingredientamount_rec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='rec',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='recipes.recipe'),
        ),
    ]