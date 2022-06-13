from django.db import models


class LowerCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()
