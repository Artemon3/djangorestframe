# Generated by Django 5.0.2 on 2024-02-19 09:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата платежа'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='payment_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма платежа'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='payment_method',
            field=models.IntegerField(blank=True, null=True, verbose_name='Метод платежа'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]