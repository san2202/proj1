# Generated by Django 3.2.5 on 2022-08-05 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user',
            new_name='username',
        ),
    ]
