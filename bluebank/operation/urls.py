from django.urls import path
from .views import home_page, transfer_money, withdraw_money

urlpatterns = [
    path("", home_page, name="home-page"),
    path("transfer_money/", transfer_money, name="transfer-money"),
    path("withdraw_money/", withdraw_money, name="withdraw-money")
]
