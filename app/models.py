from django.db import models
from django.core.validators import MinValueValidator


class Transaction(models.Model):
    payer = models.CharField(max_length=20)
    initial_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    redeemed_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    timestamp = models.DateTimeField()
