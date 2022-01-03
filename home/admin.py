from django.contrib import admin

from .models import Feed, FeedContent, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ("list_display", "description", "link", "last_build_date", "language")


@admin.register(FeedContent)
class FeedContentAdmin(admin.ModelAdmin):
    list_display = ("guid", "title", "description", "pub_date", "content_type", "feed")
