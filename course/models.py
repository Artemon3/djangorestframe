from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='courses', verbose_name='Картинка', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='courses', verbose_name='Картинка', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    url = models.URLField(max_length=200, verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'


class CoursePayment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Цена платежа', **NULLABLE)
    payment_link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='id платежа', **NULLABLE)

    def __str__(self):
        return f"{self.payment_id}"

    class Meta:
        verbose_name = 'Оплата курса'
        verbose_name_plural = 'Оплата курсов'