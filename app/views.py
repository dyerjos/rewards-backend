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
        serializer = TransactionSerializer(data=request.data)
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
            if not balance_totals.get(payer):
                balance_totals[payer] = available_points
            else:
                balance_totals[payer] += available_points
        return Response(balance_totals)


class SpendBalanceView(APIView):
    """
    Spend reward point balance.
    """

    def post(self, request, format=None):
        point_receipt = []
        points_to_spend = request.data["points"]
        transactions = Transaction.objects.filter(available_points__gt=0).order_by(
            "timestamp"
        )

        for transaction in transactions:
            if points_to_spend:
                spent_points = clamp(transaction.available_points, points_to_spend)
                points_to_spend -= spent_points
                transaction.available_points -= spent_points
                transaction.redeemed_points += spent_points
                transaction.save()
                point_receipt.append(
                    {"payer": transaction.payer, "points": -spent_points}
                )

        if points_to_spend > 0:
            point_receipt.append(
                {
                    f"{points_to_spend} points could not be spent due to a lack of reward points at this time"
                }
            )

        return Response(point_receipt)


def clamp(smallest, largest):
    return max(smallest, min(1, largest))
