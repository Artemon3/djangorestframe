# Generated by Django 5.0.2 on 2024-02-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_pay_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Никнейм'),
        ),
    ]
