# Generated by Django 3.0.8 on 2023-03-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20230302_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Наименование'),
        ),
    ]
