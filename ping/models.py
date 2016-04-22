from django.db import models

from django.conf import settings


class Ping(models.Model):
    test = models.SmallIntegerField()

    class Meta:
        db_table = 'ping'
        managed = getattr(settings, 'UNDER_TEST', False)
