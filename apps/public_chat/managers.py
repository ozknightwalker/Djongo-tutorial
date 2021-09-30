from django.db import models


class PublicRoomChatMessageManager(models.Manager):

    def by_room(self, room):
        qs = self.objects.filter(room=room).order_by("-created")
        return qs
