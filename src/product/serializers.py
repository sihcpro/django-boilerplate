from dynamic_rest.fields.fields import DynamicRelationField
from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework import serializers

from .models import Order, Product


class ProductSrl(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DynamicProductSrl(DynamicModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSrl(DynamicModelSerializer):
    product = DynamicRelationField(DynamicProductSrl)

    class Meta:
        model = Order
        fields = ["id", "product", "amount", "user", "status", "_created", "_updated"]
