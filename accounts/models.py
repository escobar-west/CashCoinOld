from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100)
