from django.http import JsonResponse
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .mixins import CustomUserAccessMixin
from .models import Order, Product
from .permissions import OnlyChangeByAdminPermission
from .serializers import OrderSrl, ProductSrl


class UserProductVS(ReadOnlyModelViewSet):
    model_class = Product
    serializer_class = ProductSrl
    queryset = Product.objects.all()
    response_class = JsonResponse


class AdminProductVS(ModelViewSet):
    model_class = Product
    serializer_class = ProductSrl
    queryset = Product.objects.all()
    response_class = JsonResponse
    permission_classes = [IsAuthenticated, OnlyChangeByAdminPermission]

    def create(self, request, *args, **kwargs):
        self.request.data["user"] = self.request.user.id
        return super().create(request, *args, **kwargs)


class OrderVS(CustomUserAccessMixin, DynamicModelViewSet):
    """Order View Set
    If you want to use one View Set for user and admin
    """

    model_class = Order
    serializer_class = OrderSrl
    queryset = Order.objects.all()
    response_class = JsonResponse
    permission_classes = [IsAuthenticated]

    def get_queryset(self, queryset=None):
        """QuerySet
        If user is not admin, that user only can view there own order.
        Returns:
            List of Orders
        """
        if self.request.user.is_superuser:
            return self.model_class.objects.all()
        else:
            return self.model_class.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        self.request.data["user"] = self.request.user.id
        return super().create(request, *args, **kwargs)
