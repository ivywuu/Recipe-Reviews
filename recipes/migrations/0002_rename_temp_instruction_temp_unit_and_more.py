# Generated by Django 4.1 on 2022-08-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instruction',
            old_name='temp',
            new_name='temp_unit',
        ),
        migrations.AddField(
            model_name='instruction',
            name='temp_num',
            field=models.IntegerField(default=0),
        ),
    ]