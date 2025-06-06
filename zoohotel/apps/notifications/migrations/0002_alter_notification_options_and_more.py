# Generated by Django 5.1.7 on 2025-04-06 16:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Уведомление', 'verbose_name_plural': 'Уведомления'},
        ),
        migrations.AlterModelOptions(
            name='notificationtype',
            options={'verbose_name': 'Тип уведомления', 'verbose_name_plural': 'Типы уведомлений'},
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['status'], name='notificatio_status_fce6f5_idx'),
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['user', 'status'], name='notificatio_user_id_8ab96f_idx'),
        ),
        migrations.AlterModelTable(
            name='notification',
            table='notifications',
        ),
        migrations.AlterModelTable(
            name='notificationtype',
            table='notification_types',
        ),
    ]
