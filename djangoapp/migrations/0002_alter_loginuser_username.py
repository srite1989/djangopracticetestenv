# Generated by Django 4.1.1 on 2022-09-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
