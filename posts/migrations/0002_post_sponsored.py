# Generated by Django 3.2.19 on 2023-05-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
    ]
