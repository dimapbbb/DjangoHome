from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'current', 'product')
