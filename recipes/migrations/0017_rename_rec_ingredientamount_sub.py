# Generated by Django 4.1 on 2022-09-11 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_subrecipe_alter_ingredientamount_rec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientamount',
            old_name='rec',
            new_name='sub',
        ),
    ]
