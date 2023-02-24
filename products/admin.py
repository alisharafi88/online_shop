from django.contrib import admin
from .models import Product, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment
    fields = ['product', 'user', 'text', 'point', 'active']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentsInLine,
    ]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'point', 'active']
