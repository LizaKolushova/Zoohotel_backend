# Generated by Django 5.1.7 on 2025-04-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Животное', 'verbose_name_plural': 'Животные'},
        ),
        migrations.AlterModelOptions(
            name='animalpassport',
            options={'verbose_name': 'Паспорт животного', 'verbose_name_plural': 'Паспорта животных'},
        ),
        migrations.AlterModelOptions(
            name='animaltype',
            options={'verbose_name': 'Тип животного', 'verbose_name_plural': 'Типы животных'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='treatment',
            options={'verbose_name': 'Лечение', 'verbose_name_plural': 'Лечения'},
        ),
        migrations.AlterModelOptions(
            name='vaccination',
            options={'verbose_name': 'Вакцинация', 'verbose_name_plural': 'Вакцинации'},
        ),
        migrations.AddIndex(
            model_name='treatment',
            index=models.Index(fields=['animal', 'treatment_date'], name='treatments_animal__96e0fa_idx'),
        ),
        migrations.AddIndex(
            model_name='vaccination',
            index=models.Index(fields=['animal', 'vaccination_date'], name='vaccination_animal__cf397e_idx'),
        ),
        migrations.AlterModelTable(
            name='animal',
            table='animals',
        ),
        migrations.AlterModelTable(
            name='animalpassport',
            table='animal_passports',
        ),
        migrations.AlterModelTable(
            name='animaltype',
            table='animal_types',
        ),
        migrations.AlterModelTable(
            name='client',
            table='clients',
        ),
        migrations.AlterModelTable(
            name='treatment',
            table='treatments',
        ),
        migrations.AlterModelTable(
            name='vaccination',
            table='vaccinations',
        ),
    ]
