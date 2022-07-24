from django.db import models

class UserModel(models.Model):
    username = models.TextField(max_length=100)
    pass1 = models.TextField(max_length=100)
    pass2 = models.TextField(max_length=100)