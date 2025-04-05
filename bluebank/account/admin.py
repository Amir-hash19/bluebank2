from django.contrib import admin
from .models import Account



@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "create_at")
    ordering = ("-create_at", )
    list_filter = ("create_at", )
    search_fields = ("full_name", "email", "age")


