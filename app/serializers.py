from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    points = serializers.IntegerField(source="initial_points")

    class Meta:
        model = Transaction
        fields = ("payer", "points", "timestamp")
