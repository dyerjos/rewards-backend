from .models import Transaction
from .serializers import TransactionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TransactionList(APIView):
    """
    List all snippets, or create a new transaction."""

    def get(self, request, format=None):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BalanceView(APIView):
    """
    Return current reward point balance.
    """

    def get(self, request, format=None):
        transactions = Transaction.objects.values()
        balance_totals = {}
        for transaction in transactions:
            payer = transaction["payer"].upper()
            available_points = transaction["available_points"]
            if not hasattr(balance_totals, payer):
                balance_totals[payer] = available_points
            else:
                balance_totals[payer] += available_points
        return Response(balance_totals)
