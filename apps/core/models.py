from hashid_field import HashidAutoField  # Hashid, HashidField

from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UndeletedManager


class AbstractCreatedDateMixin(models.Model):
    created_at = models.DateTimeField(_("created"), auto_now_add=True)

    class Meta:
        abstract = True


class AbstractUpdatedDateMixin(models.Model):
    updated_at = models.DateTimeField(_('updated'), auto_now=True, blank=True)

    def save(self, *args, **kwargs):
        # Force date update
        if self.pk:
            kwargs['update_fields'] = kwargs.get(
                'update_fields', []).append('updated_at')
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class AbstractCreatedUpdatedDateMixin(
        AbstractCreatedDateMixin, AbstractUpdatedDateMixin):

    class Meta:
        abstract = True


class AbstractDeletableMixin(models.Model):
    deleted_at = models.DateTimeField(
        _('deleted'), null=True, blank=True, db_index=True)

    # managers
    objects = models.Manager()
    valid_objects = UndeletedManager()

    def is_deleted(self):
        return self.deleted_at is not None

    is_deleted.boolean = True

    def soft_delete(self):
        self._meta.model.objects.filter(
            id=self.id, deleted_at__isnull=True).update(
            deleted_at=timezone.now())

    class Meta:
        abstract = True


class AbstractUniqueHashIDMixin(models.Model):
    id = HashidAutoField(primary_key=True)

    class Meta:
        abstract = True
