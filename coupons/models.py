from django.db import models

class Coupon(models.Model):
    key_val = models.CharField(max_length=30)
    value = models.FloatField()
