# Generated by Django 3.2.5 on 2022-08-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('contact', models.PositiveBigIntegerField()),
                ('user', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('password1', models.CharField(max_length=40)),
            ],
        ),
    ]
