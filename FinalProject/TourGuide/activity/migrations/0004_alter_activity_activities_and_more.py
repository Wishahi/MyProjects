# Generated by Django 4.1 on 2022-09-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_activity_photo_10_activity_photo_11_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activities',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='activity',
            name='places_to_visit',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='activity',
            name='restaurants',
            field=models.TextField(max_length=1000),
        ),
    ]
