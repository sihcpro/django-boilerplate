from app.logger import logger
from django.contrib.auth.models import User


def create_admin():
    def _create_admin():
        user = User.objects.filter(username="admin").first()
        if user is None:
            user: User = User.objects.create(
                username="admin",
                email="admin@yopmail.com",
                is_staff=True,
                is_superuser=True,
            )
            user.set_password("admin123")
            user.save()
        return user

    try:
        return _create_admin()
    except Exception as e:
        logger.error("Can't create admin")
        logger.exception(e)
