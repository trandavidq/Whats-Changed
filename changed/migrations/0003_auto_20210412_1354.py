# Generated by Django 3.1.6 on 2021-04-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changed', '0002_auto_20210412_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='average_rating',
            field=models.FloatField(),
        ),
    ]