# Generated by Django 5.2.3 on 2025-06-27 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacramentos', '0002_bautismo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bautizo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(help_text='Ej: 12345678-9', max_length=12)),
                ('nombre_completo', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('celebrante', models.CharField(max_length=100)),
                ('iglesia', models.CharField(max_length=100)),
                ('padrinos', models.TextField()),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bautismo',
        ),
        migrations.DeleteModel(
            name='Sacramento',
        ),
    ]
