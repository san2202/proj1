# Generated by Django 3.2.5 on 2022-09-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_student1_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student1',
            name='fee',
            field=models.PositiveIntegerField(),
        ),
    ]
