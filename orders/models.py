from django.db import models

# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
    

class Item(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} ({self.quantity})"
