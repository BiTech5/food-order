from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the orders index.")

