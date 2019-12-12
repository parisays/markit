from django.db import models
# Using FieldTracker from django-model-utils helps you only send
# updates when something actually changes.
from model_utils import FieldTracker
from asgiref.sync import async_to_sync
from .views import update_foo

class Foo(models.Model):
    tracker = FieldTracker(fields=("bar",))
    bar = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        ret = super().save(*args, **kwargs)
        has_changed = self.tracker.has_changed("bar")
        if has_changed:
            # This is the wrapper that lets you call an async
            # function from inside a synchronous context:
            async_to_sync(update_foo)(self)
        return ret