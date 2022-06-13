from app.logger import logger
from rest_framework.permissions import BasePermission


class OnlyChangeByAdminPermission(BasePermission):
    def has_permission(self, request, view):
        logger.warning("Checking permissions")
        if request.method == "GET":
            return True
        else:
            return bool(request.user and request.user.is_staff)
