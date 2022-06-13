from django.db.models import CharField, IntegerField
from django_mysql.models.fields.lists import ListFieldMixin


class ListIntegerField(ListFieldMixin, IntegerField):
    pass
