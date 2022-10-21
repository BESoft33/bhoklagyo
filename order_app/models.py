from django.db import models

from food_app.models import Food
from user_app.models import Customer

class Order(models.Model):
    DELIVERED   = 'delivered'
    ACCEPTED    = 'success'
    REJECTED    = 'failed'
    PENDING     = 'pending'
    CANCELLED   = 'cancelled'

    ORDER_STATUS ={
        (DELIVERED, 'Delivered'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
        (CANCELLED, 'Cancelled')
    }

    user = models.ForeignKey(to = Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(to = Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length = 20, choices = ORDER_STATUS, default = PENDING)
    request_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.user}-{self.id}"

    class Meta:
        db_table = 'orders'

class Cart(models.Model):
    user = models.ForeignKey(to = Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(to = Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}-{self.id}"

    class Meta:
        db_table = 'cart'

class BillingLocation(models.Model):
    address = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    request_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField()

    class Meta:
        db_table = 'billing_location'