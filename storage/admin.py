from django.contrib import admin
from storage.models import Product, Category, Position, Stock


@admin.register(Product)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class PositionInline(admin.TabularInline):
    model = Position
    extra = 0


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']
    inlines = [PositionInline]
