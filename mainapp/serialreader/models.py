from django.db import models

class SerialModel(models.Model):
    distance1 = models.CharField(max_length=1000, default="empty")
    distance2 = models.CharField(max_length=1000, default="empty")
    distance3 = models.CharField(max_length=1000, default="empty")
    distance4 = models.CharField(max_length=1000, default="empty")