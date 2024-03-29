from datetime import datetime, timedelta

from celery import shared_task

from users.models import User


@shared_task
def block_user():
    users = User.objects.filter(last_login__lte=datetime.now()-timedelta(days=30))
    if users.exists():
        users.update(is_active=False)