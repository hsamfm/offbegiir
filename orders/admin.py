# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'did',
        'datetime',
        'customerid',
        'payid',
        'pay_amount',
    )
    list_filter = ('did', 'datetime')
