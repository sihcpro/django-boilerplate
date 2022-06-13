from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.base import ModelBase
from django.db.models.manager import Manager

from .lookup import NotEqual

models.Field.register_lookup(NotEqual)


class SManager(Manager):
    def get_if_exist(self, *args: Any, **kwargs: Any):
        try:
            return self.get(*args, **kwargs)
        except ObjectDoesNotExist:
            return None


class SModelBase(ModelBase):
    def _prepare(cls):
        manager = SManager()
        manager.auto_created = True
        cls.add_to_class("objects", manager)

        super()._prepare()

    class Meta:
        abstract = True


class SModel(models.Model, metaclass=SModelBase):

    managers = False
    objects: SManager

    # For serializer
    PERSONAL_FIELDS = []  # is a list of fields that don't show in public
    SYSTEM_FIELDS = []  # is a list of fields that not allow to update by user

    # For model
    READONLY_FIELDS = []  # is a list of fields that not allow to update
    FILTER_FIELDS = {}

    def get_readonly_fields(self, request, obj=None):
        return self.READONLY_FIELDS

    @classmethod
    def _all_fields(cls) -> list:
        return [i.name for i in cls._meta.concrete_fields]

    class Meta:
        abstract = True
