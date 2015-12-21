# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from celery_app.models import CeleryApp

admin.site.register(CeleryApp)