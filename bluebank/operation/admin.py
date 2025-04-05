from django.contrib import admin
from operation.models import BankAccount, Transaction


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email", "create_at")
    ordering = ("-create_at", "balance")
    list_filter = ("create_at", )
    search_fields = ("full_name", "email", "balance")




@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("account", "amount", "description")
    ordering = ("-amount", )
    list_filter = ("amount", "account", "transaction_type")
    search_fields = ("account", "transaction_type")
