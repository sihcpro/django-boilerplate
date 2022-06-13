from typing import Optional

from app.logger import logger
from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin
from django.http import JsonResponse


class CustomUserAccessMixin(UserPassesTestMixin):
    USER_ALLOWED_METHODS = {"GET"}
    EXCEPTION_MESSAGE = "You are not allowed to do this action."

    def dispatch(self, request, *args, **kwargs):
        return super(AccessMixin, self).dispatch(request, *args, **kwargs)

    def test_func(self) -> Optional[bool]:
        if self.request.method in {"GET", "POST"}:
            return True
        self.request.user.is_authenticated
        return self.request.user.is_authenticated and self.request.user.is_staff

    def handle_no_permission(self):
        return JsonResponse(data={"message": self.EXCEPTION_MESSAGE})
