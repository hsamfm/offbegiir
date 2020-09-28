# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'password',
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'email',
        'name',
        'last_name',
        'mobile',
        'uname',
        'uid',
        'date_reg',
        'shop_id',
        'cart_number',
        'id_moaref',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_reg',
    )
    raw_id_fields = ('groups', 'user_permissions')
    search_fields = ('name',)
