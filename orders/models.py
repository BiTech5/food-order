from django.db import models


# Create your models here.
class Order(models.Model):
    """
    Represents a customer order in the system.
    
    Fields:
    - customer_name (str): Name of the customer placing the order
    - customer_email (str): Email address of the customer
    - item (str): Name/description of the ordered item
    - quantity (int): Number of items ordered (defaults to 1)
    - price (Decimal): Price per unit of the item
    - total_price (Decimal): Total price of the order (price * quantity)
    - order_date (datetime): Timestamp when order was placed
    - shipping_address (str): Delivery address for the order
    - status (str): Current status of the order (defaults to 'pending')
    """
    order_id: models.AutoField = models.AutoField(primary_key=True)
    customer_name: models.CharField = models.CharField(max_length=200)
    customer_email: models.EmailField = models.EmailField(max_length=200)
    item: models.CharField = models.CharField(max_length=200)
    quantity: models.IntegerField = models.IntegerField(default=1)
    price: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)
    total_price: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)
    order_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    shipping_address: models.CharField = models.CharField(max_length=200)
    STATUS_CHOICES: list[tuple[str, str]] = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    status: models.CharField = models.CharField(max_length=200, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self) -> str:
        return f"{self.customer_name} ordered {self.item} x {self.quantity}"
