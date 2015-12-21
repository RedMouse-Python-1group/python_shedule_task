# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class CeleryApp(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)

    def __unicode__(self):
        return self.field1