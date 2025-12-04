from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    color=models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('products',blank=True)
    

    def __str__(self):
        return f"{self.product.name} Image"


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=255)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    color = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} by {self.name}"
