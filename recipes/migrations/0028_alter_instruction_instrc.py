# Generated by Django 4.1 on 2022-08-25 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0027_alter_instructioningredient_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='instrc',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='recipes.simpleinstruction'),
        ),
    ]
