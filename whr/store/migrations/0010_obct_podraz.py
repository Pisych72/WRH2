# Generated by Django 3.0.8 on 2023-02-27 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_obct'),
    ]

    operations = [
        migrations.AddField(
            model_name='obct',
            name='podraz',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='store.Podraz', verbose_name='Подразделение'),
            preserve_default=False,
        ),
    ]
