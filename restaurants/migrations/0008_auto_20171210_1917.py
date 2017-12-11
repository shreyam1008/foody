# Generated by Django 2.0 on 2017-12-10 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20171210_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]