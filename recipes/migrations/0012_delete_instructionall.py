# Generated by Django 4.1 on 2022-08-24 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_remove_instruction_time_instruction_time_num_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InstructionAll',
        ),
    ]
