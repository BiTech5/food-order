from django.shortcuts import render
from django.shortcuts import redirect
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
    if request.method == 'POST':
        # Get form data
        customer_name: str = request.POST['customer_name']
        customer_email: str = request.POST['customer_email'] 
        item: str = request.POST['item']
        quantity: int = int(request.POST['quantity'])
        price: float = float(request.POST['price'])
        shipping_address: str = request.POST['shipping_address']
        
        # Calculate total price
        total_price: float = quantity * price
        
        # Create and save new order
        order: Order = Order(
            customer_name=customer_name,
            customer_email=customer_email,
            item=item,
            quantity=quantity,
            price=price,
            total_price=total_price,
            shipping_address=shipping_address
        )
        order.save()
        
        # Redirect to order list
        return redirect('list_orders')
        
    return render(request, 'orders/create_order.html')

def update_order(request: HttpRequest) -> HttpResponse:
    return render(request,"orders/update_order.html")
def delete_order(request: HttpRequest) -> HttpResponse:
    pass
