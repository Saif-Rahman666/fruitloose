# Generated by Django 4.1.6 on 2023-05-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruitmodel',
            name='spoiled',
            field=models.BooleanField(default=False, verbose_name='Spoiled'),
        ),
    ]
