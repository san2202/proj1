# Generated by Django 3.2.5 on 2022-08-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20220817_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('std_image', models.ImageField(upload_to='media/images/')),
                ('std_profile', models.FileField(upload_to='media/files/')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student3',
        ),
    ]
