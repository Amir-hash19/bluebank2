from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Transaction, BankAccount
from account.models import Account
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def home_page(request):
    return HttpResponse("this is oprations page")




@csrf_exempt
def transfer_money(from_account, to_account, amount):
    if from_account.balance < amount:
        raise ValueError("Insufficient funds")
    
    from_account.balance -= amount
    to_account.balance += amount

    from_account.save()
    to_account.save()

    Transaction.objects.create(
        account=from_account,
        transaction_type='transfer',
        amount=amount,
        to_account=to_account,
        description=f"Transaction to{to_account.full_name}"
    )






@csrf_exempt
def withdraw_money(account: Account, amount: float, description: str = ""):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if account.balance < amount:
        raise ValueError("Insufficient funds.")

   
    account.balance -= amount
    account.save()

  
    Transaction.objects.create(
        account=account,
        transaction_type='withdraw',
        amount=amount,
        description=description or "Withdrawal",
        timestamp=timezone.now()
    )

    return True

