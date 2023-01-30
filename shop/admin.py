from django.contrib import admin
from .models import Product, Category, Brand, Review, Inquiry, Like, Cart, CategoryJP

admin.site.register(Product)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdminJP(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CategoryJP, CategoryAdminJP)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Review)
admin.site.register(Inquiry)
admin.site.register(Like)
admin.site.register(Cart)
