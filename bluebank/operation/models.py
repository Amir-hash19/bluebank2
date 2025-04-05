from django.db import models
from account.models import Account
from phonenumber_field.modelfields import PhoneNumberField



class BankAccount(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True, region="IR")
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.balance}"
    



class Transaction(models.Model):
        TRANSACTION_TYPE_CHOICES = [
             ('deposit', 'واریز'),
             ('withdraw', 'برداشت'),
             ('transfer', 'انتقال'),
             ]
        
        account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
        transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
        amount = models.DecimalField(max_digits=15, decimal_places=2)
        timestamp = models.DateTimeField(auto_now_add=True)
        description = models.TextField(blank=True, null=True)
        to_account = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True,related_name='received_transfers')


        
    
        def __str__(self):
            return f"{self.account.full_name} - {self.transaction_type} - {self.amount}"
