# Generated by Django 3.1.6 on 2021-04-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_pid',
            field=models.TextField(default='no pid'),
            preserve_default=False,
        ),
    ]
