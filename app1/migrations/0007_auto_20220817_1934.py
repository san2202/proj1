# Generated by Django 3.2.5 on 2022-08-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_student2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('std_image', models.ImageField(upload_to='media/images/')),
                ('std_profile', models.FileField(upload_to='media/files/')),
            ],
        ),
        migrations.DeleteModel(
            name='Student2',
        ),
    ]