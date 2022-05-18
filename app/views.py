from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
