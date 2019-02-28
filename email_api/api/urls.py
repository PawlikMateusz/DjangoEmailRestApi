from django.urls import path

from .views import test_view

app_name = "api"

urlpatterns = [
    path("", view=test_view, name="test"),

]
