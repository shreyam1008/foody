# Generated by Django 2.0.5 on 2018-08-08 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('comment_head', models.CharField(blank=True, max_length=50, null=True)),
                ('comment_body', models.CharField(blank=True, max_length=150, null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foo', to='foods.Food')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rest', to='restaurants.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('comment_head', models.CharField(blank=True, max_length=50, null=True)),
                ('comment_body', models.CharField(blank=True, max_length=150, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restau', to='restaurants.Restaurant')),
            ],
        ),
    ]
