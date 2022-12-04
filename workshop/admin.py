from django.contrib import admin

from workshop.models import Office, FireExtingusher, OrderPosition, Order, Firm


@admin.register(Office)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['firm', 'adress']


@admin.register(FireExtingusher)
class FireExtingusherAdmin(admin.ModelAdmin):
    list_display = ['type', 'weight', 'repair_coast']


class QuantityInline(admin.TabularInline):
    model = OrderPosition
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'status', 'date_input']
    inlines = [QuantityInline]


@admin.register(Firm)
class Firm(admin.ModelAdmin):
    list_display = ['name']
