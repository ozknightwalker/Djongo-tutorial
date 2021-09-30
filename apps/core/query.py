from django.db.models.query import QuerySet
from django.utils import timezone


class UndeletedQuerySet(QuerySet):

    def soft_delete(self, **kwargs):
        return self.update(delete_ts=timezone.now(), **kwargs)
