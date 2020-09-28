# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Doll


@admin.register(Doll)
class DollAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'group',
        'picture',
        'datetime',
        'price',
        'shop_id',
        'using_datetime',
        'tel',
        'address',
        'click',
        'alt',
        'x',
        'y',
        'meta_word',
        'meta_description',
        'doll_count',
    )
    list_filter = ('group', 'datetime', 'shop_id')
    search_fields = ('name',)
