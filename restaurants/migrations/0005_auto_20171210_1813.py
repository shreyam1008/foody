# Generated by Django 2.0 on 2017-12-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20171210_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
