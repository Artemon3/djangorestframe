from datetime import datetime, timedelta

from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils import timezone

from course.models import Subscription


@shared_task
def material_update():
    # subscript = Subscription.objects.get(course_id=course_id)
    # for sub in subscript:
    #     if sub.course.last_update < timezone.now():
    #         send_mail(
    #             subject='Обновление курса',
    #             message=f'Курс {sub.course.title} был обновлен',
    #             from_email=EMAIL_HOST_USER,
    #             recipient_list=[sub.user.email]
    #         )
    print('Task open')
    for sub in Subscription.objects.filter(course__last_update__gte=datetime.now()-timedelta(minutes=1)):
        send_mail(
                    subject='Обновление курса',
                    message=f'Курс {sub.course.title} был обновлен',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[sub.user.email]
                )
        print("Send mail")

