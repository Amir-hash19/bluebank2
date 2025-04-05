from django.shortcuts import render
from django.http.response import HttpResponse


def display_home(request):
    return HttpResponse("This is home page")
   

