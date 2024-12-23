from django.db import models


# Create your models here.
class Order(models.Model):
    """
    Represents a customer order in the system.
    
    Fields:
    - customer_name: Name of the customer placing the order
    - customer_email: Email address of the customer
    - item: Name/description of the ordered item
    - quantity: Number of items ordered (defaults to 1)
    - price: Price per unit of the item
    - total_price: Total price of the order (price * quantity)
    - order_date: Timestamp when order was placed
    - shipping_address: Delivery address for the order
    - status: Current status of the order (defaults to 'pending')
    """
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    item = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='pending')
    
    def __str__(self) -> str:
        return f"{self.customer_name} ordered {self.item} x {self.quantity}"
