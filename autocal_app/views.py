from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(repuest):
    return HttpResponse("Hello, world. You're at the autocal_app index.")

def calculate(repuest,expr):
    response = "You typed " + expr + "."
    return HttpResponse(response)
