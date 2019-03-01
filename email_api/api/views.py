from django.http import HttpResponse
from rest_framework import viewsets, mixins

from .tasks import test_email_task
from .models import Email, Mailbox, Template
from .serializers import EmailSerializer, TemplateSerializer, MailboxSerializer


class MailboxViewSet(viewsets.ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class EmailViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        print("hello world!!!!!")
        return super(EmailViewSet, self).create(request, *args, **kwargs)
