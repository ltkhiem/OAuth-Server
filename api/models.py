from django.db import models
import time


class Document(models.Model):
    client_state = models.CharField(max_length=255, default='')
    timestamp = models.FloatField(default=time.time())
    access_token = models.CharField(max_length=255, default='')
    refresh_token = models.CharField(max_length=255, default='')