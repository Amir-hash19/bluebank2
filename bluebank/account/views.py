from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Account
import json



def display_home(request):
    return HttpResponse("This is home page")
   


@csrf_exempt
def create_account(request):
    if request.method == "POST":
        data = json.loads(request.body)
        created_account = Account.objects.create(
            full_name = data.get("full_name"),
            email = data.get("email"),
            age = data.get("age"),
            phone_number = data.get("phone_number")
        )
        return HttpResponse(f"The User with ID {created_account.id} created Successfully!")
    



@csrf_exempt
@require_http_methods(["GET"])
def display_account(request, account_id):
    try:
        account = Account.objects.get(id=account_id)
        account_data = {
            "id":account.id,
            "full_name":account.full_name,
            "email":account.email,
            "age":account.age,
            "phone_number":str(account.phone_number)
        }
        return JsonResponse(account_data)
    except Account.DoesNotExist:
        return HttpResponse("The User Does not existed!")
    
    

    
@csrf_exempt
def remove_account(request, account_id):
    if request.method == "DELETE":
        account = Account.objects.get(id=account_id)
        account.delete()
        return HttpResponse("The Account Deleted Successfully!")



