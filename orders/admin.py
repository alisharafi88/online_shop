from django.contrib import admin
from .models import Order, ItemOrder


class ItemsInLine(admin.TabularInline):
    model = ItemOrder
    fields = ['order', 'product', 'quantity', 'price']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'is_paid',
        'first_name',
        'last_name',
        'phone_number',
        'address',
        'order_nots',
        'datetime_created',
        'datetime_modified'
    ]
    inlines = [
        ItemsInLine,
    ]


@admin.register(ItemOrder)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
