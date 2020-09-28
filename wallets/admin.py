# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'value', 'test', 'pay_id')
