from django.contrib import admin
from .models import Faq, Category, FaqJP, CategoryJP

class FaqAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "author", "created", "updated")
    readonly_fields = ("created", "updated")

    fieldsets = (
        ("정보", {
            "fields": ("category", "question", "answer")
        }),
        ("부가 정보", {
            "fields": ("author", "created", "updated")
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "author", "created", "updated")
    readonly_fields = ("created", "updated")

    fieldsets = (
        ("정보", {
            "fields": ("category",)
        }),
        ("부가 정보", {
            "fields": ("author", "created", "updated")
        }),
    )


class FaqAdminJP(admin.ModelAdmin):
    list_display = ("question", "category", "author", "created", "updated")
    readonly_fields = ("created", "updated")

    fieldsets = (
        ("정보", {
            "fields": ("category", "question", "answer")
        }),
        ("부가 정보", {
            "fields": ("author", "created", "updated")
        }),
    )


class CategoryAdminJP(admin.ModelAdmin):
    list_display = ("category", "author", "created", "updated")
    readonly_fields = ("created", "updated")

    fieldsets = (
        ("정보", {
            "fields": ("category",)
        }),
        ("부가 정보", {
            "fields": ("author", "created", "updated")
        }),
    )


admin.site.register(Faq, FaqAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FaqJP, FaqAdminJP)
admin.site.register(CategoryJP, CategoryAdminJP)
