# Generated by Django 3.2.5 on 2022-08-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('sid', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('sname', models.CharField(max_length=40)),
                ('time', models.TimeField()),
                ('fee', models.FloatField()),
                ('doj', models.DateField()),
                ('dov', models.DateTimeField()),
                ('dur', models.DurationField()),
                ('history', models.BooleanField()),
            ],
        ),
    ]
