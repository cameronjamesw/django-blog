# Generated by Django 4.2.11 on 2024-05-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
