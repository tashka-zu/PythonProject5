from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from materials.models import Subscription
from .models import Course
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_course_update_email(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course)
    for subscription in subscriptions:
        send_mail(
            subject=f"Обновление курса: {course.name}",
            message=f"Курс {course.name} был обновлён. Загляните на платформу, чтобы ознакомиться с изменениями.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscription.user.email],
            fail_silently=False,
        )


@shared_task
def deactivate_inactive_users():
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)
    for user in inactive_users:
        user.is_active = False
        user.save()
