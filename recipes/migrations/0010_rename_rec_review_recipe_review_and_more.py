# Generated by Django 4.1 on 2022-08-16 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_rename_ingr_brand_ingredient_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='rec_review',
            new_name='review',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='rec_title',
            new_name='title',
        ),
    ]
