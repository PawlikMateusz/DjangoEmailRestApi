from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def test_email_task():
    send_mail(
        'Subject here',
        'Here is the MYYYYY! message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
