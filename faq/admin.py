from django.contrib import admin
from .models import Faq, Category

class FaqAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "author", "created", "updated")
    readonly_fields = ("created", "updated")

    fieldsets = (
        ("情報", {
            "fields": ("category", "question", "answer")
        }),
        ("付加情報", {
            "fields": ("author", "created", "updated")
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "author", "created", "updated")
    readonly_fields = ("created", "updated")

    fieldsets = (
        ("情報", {
            "fields": ("category",)
        }),
        ("付加情報", {
            "fields": ("author", "created", "updated")
        }),
    )


admin.site.register(Faq, FaqAdmin)
admin.site.register(Category, CategoryAdmin)
