from django.urls import path

from .views import TransactionList

urlpatterns = [
    path("", TransactionList.as_view(), name="home"),
]
