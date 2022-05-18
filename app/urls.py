from django.urls import path

from .views import (
    TransactionList,
    BalanceView,
    SpendBalanceView,
)

urlpatterns = [
    path("", TransactionList.as_view(), name="home"),
    path("get_balance", BalanceView.as_view(), name="current balance"),
    path("spend_points", SpendBalanceView.as_view(), name="spend points"),
]
