# Generated by Django 4.1 on 2022-08-25 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_simpleinstruction_alter_ingredientamount_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='instr',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.simpleinstruction'),
        ),
    ]