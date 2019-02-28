from django.http import HttpResponse

from .tasks import test_email_task


def test_view(request):
    test_email_task.delay()
    return HttpResponse(content='Witamy w moim api!')
