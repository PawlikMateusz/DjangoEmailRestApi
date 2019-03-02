from django.http import HttpResponse
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .tasks import send_email
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
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_email.apply_async(
                (request.data, serializer.instance.id), retry=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
