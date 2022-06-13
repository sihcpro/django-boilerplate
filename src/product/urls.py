from django.conf.urls import include, url
from dynamic_rest.routers import DynamicRouter
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("product", views.UserProductVS, basename="product")
router.register("order", views.OrderVS, basename="order")

admin_router = DefaultRouter()
admin_router.register("product", views.AdminProductVS, basename="admin product")

urlpatterns = [
    url(r"", include(router.urls)),
]

admin_urlpatterns = [
    url("", include(admin_router.urls)),
]
