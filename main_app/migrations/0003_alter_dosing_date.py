# Generated by Django 5.2 on 2025-05-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_dosing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosing',
            name='date',
            field=models.DateField(verbose_name='Dosage Date'),
        ),
    ]
