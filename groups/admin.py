# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import FGroup


@admin.register(FGroup)
class FGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'g_id', 'picture', 'name', 'count')
    search_fields = ('name',)
