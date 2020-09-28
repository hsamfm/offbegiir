# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Admin


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'uname', 'date_registered')
    list_filter = ('date_registered',)
