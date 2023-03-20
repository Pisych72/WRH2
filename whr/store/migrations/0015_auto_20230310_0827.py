# Generated by Django 3.0.8 on 2023-03-10 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20230309_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurnal',
            name='fio',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to='store.Fio', verbose_name='Подотчет'),
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='obct',
            field=models.ForeignKey(default=180, on_delete=django.db.models.deletion.PROTECT, to='store.Obct', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='podraz',
            field=models.ForeignKey(default=74, on_delete=django.db.models.deletion.PROTECT, to='store.Podraz', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='postav',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, to='store.Postav', verbose_name='Поставщик'),
        ),
        migrations.CreateModel(
            name='JurnalDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oper', models.IntegerField(max_length=1, verbose_name='Операция')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
                ('summa', models.FloatField(verbose_name='Сумма')),
                ('nds', models.IntegerField(default=20, verbose_name='НДС')),
                ('summawithnds', models.FloatField(verbose_name='Сумма с НДС')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Создан')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')),
                ('uniqfield', models.CharField(max_length=250, verbose_name='Слаг')),
                ('fio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Fio', verbose_name='Подотчетник')),
                ('iddoc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Jurnal')),
                ('obct', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Obct', verbose_name='Объект')),
                ('podraz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Podraz', verbose_name='Подразделение')),
                ('postav', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Postav', verbose_name='Поставщик')),
                ('spis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.Spis', verbose_name='Причина списания')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Nom', verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Табличная часть',
                'verbose_name_plural': 'Табличные части',
                'ordering': ['-created_at'],
            },
        ),
    ]
