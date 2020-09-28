# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'tel', 'dt', 'user_id')
    list_filter = ('dt', 'user_id')
    search_fields = ('name',)

