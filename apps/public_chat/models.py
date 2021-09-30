from django.db import models
from django.conf import settings

from apps.core.models import (
    AbstractUniqueHashIDMixin,
    AbstractCreatedDateMixin,
)

from .managers import PublicRoomChatMessageManager


class PublicChatRoom(AbstractUniqueHashIDMixin, models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.title

    def connect_user(self, user):
        connected = False

        if not self.users.filter(id=user.id).exists():
            self.users.add(user)
            self.save(updated_fields=["users"])
            connected = True
        else:
            connected = True
        return connected

    def disconnect_user(self, user):
        removed = False
        if self.users.filter(id=user.id).exists():
            self.users.remove(user)
            self.save(updated_fields=["users"])
            removed = True
        return removed

    @property
    def group_name(self):
        return f"PublicCharRoom-{self.id}"


class PublicRoomChatMessage(
        AbstractUniqueHashIDMixin, AbstractCreatedDateMixin, models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    content = models.TextField(unique=False, blank=False)
    objects = PublicRoomChatMessageManager()

    def __str__(self):
        return self.content