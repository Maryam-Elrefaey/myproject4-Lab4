from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('CLOT', 'Clothes'),
        ('BOOK', 'Books'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name="Product Name",
        help_text="Enter the product name"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Enter the price in USD"
    )
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='ELEC'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # ✅ مع باقي الفيلدز

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Test(models.Model):
    data = models.DateField()
    time = models.TimeField(null=True, blank=True)
    created = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return str(self.data)
