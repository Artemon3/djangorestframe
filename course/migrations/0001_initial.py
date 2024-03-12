# Generated by Django 5.0.2 on 2024-02-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses', verbose_name='Картинка')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('url', models.URLField(verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses', verbose_name='Картинка')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('lesson', models.ManyToManyField(to='course.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
    ]
