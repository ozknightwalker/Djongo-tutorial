from django.contrib import admin

from apps.core.paginator import AdminCachingPaginator

from .models import PublicChatRoom, PublicRoomChatMessage


class PublicChatRoomAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["id", "title"]

    class Meta:
        model = PublicChatRoom


class PublicRoomChatMessageAdmin(admin.ModelAdmin):
    list_filter = ["room", "user", "created_at"]
    list_display = ["room", "user", "created_at", "content"]
    search_fields = ["room__title", "user__username", "content"]
    readonly_fields = ["id", "user", "room", "created_at"]

    show_full_result_count = False
    paginator = AdminCachingPaginator

    class Meta:
        model = PublicRoomChatMessage


admin.site.register(PublicChatRoom, PublicChatRoomAdmin)
admin.site.register(PublicRoomChatMessage, PublicRoomChatMessageAdmin)
