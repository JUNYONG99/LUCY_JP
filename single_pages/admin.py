from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "created", "updated")
    readonly_fields = ("created", "updated")

    fieldsets = (
        ("정보", {
            "fields": ("title", "content")
        }),
        ("부가 정보", {
            "fields": ("author", "created", "updated")
        }),
    )

admin.site.register(About, AboutAdmin)