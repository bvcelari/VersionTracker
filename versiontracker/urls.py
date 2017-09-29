from django.conf.urls import url
from django.contrib import admin
from .models import *

urlpatterns = [
    url(r'^adminversiontracker/', admin.site.urls),
]

