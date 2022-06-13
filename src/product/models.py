from custom_django.helper import create_admin
from custom_django.models import fields
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

if settings.AUTO_CREATE_ADMIN:
    create_admin()


class Product(models.Model):
    ACTIVE = "A"
    INACTIVE = "I"
    STATUS = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    )

    FOOD = "F"
    GOOD = "G"
    TYPES = (
        (FOOD, "Food"),
        (GOOD, "Good"),
    )

    user = models.ForeignKey(User, models.CASCADE)

    name = models.CharField(max_length=255)

    status = models.CharField(max_length=1, default=ACTIVE, choices=STATUS)
    type = models.CharField(max_length=1, default=GOOD, choices=TYPES)

    _created = fields.UnixTimeStampField(null=True, auto_now_add=True)
    _updated = fields.UnixTimeStampField(null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = "Product"


class Order(models.Model):
    ORDERD = "O"
    COMPLEATED = "P"
    CANCELLED = "C"
    STATUS = (
        (ORDERD, "Orderd"),
        (COMPLEATED, "Compleated"),
        (CANCELLED, "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    status = models.CharField(max_length=1, default=ORDERD, choices=STATUS)

    amount = models.IntegerField()

    _created = fields.UnixTimeStampField(null=True, auto_now_add=True)
    _updated = fields.UnixTimeStampField(null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = "Order"
