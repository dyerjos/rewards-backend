from django.db import models
from django.core.validators import MinValueValidator


class Transaction(models.Model):
    payer = models.CharField(max_length=20)
    initial_points = models.IntegerField(validators=[MinValueValidator(0)])
    redeemed_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    available_points = models.IntegerField(
        default=None, validators=[MinValueValidator(0)]
    )
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.available_points == None:
            self.available_points = self.initial_points
        super().save(*args, **kwargs)
