from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=850)
    price = models.FloatField()
    description = models.TextField(max_length=80)
    imglink = models.CharField(max_length=850)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    address = models.CharField(max_length=600)
    city = models.CharField(max_length=400)
    payment_method = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400)
    items = models.TextField()
    fulfilled = models.BooleanField(default=False)
