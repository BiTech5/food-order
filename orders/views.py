from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Order
# Create your views here.
def list_orders(request: HttpRequest) -> HttpResponse:
    data: dict[str, list[Order]] = {
        'orders': Order.objects.all()
    }
    return render(request, 'orders/order_view.html', data)

def create_order(request: HttpRequest) -> HttpResponse:
    return render(request,'orders/create_order.html')
def update_order(request: HttpRequest) -> HttpResponse:
    pass
def delete_order(request: HttpRequest) -> HttpResponse:
    pass
