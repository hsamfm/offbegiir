# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'topic',
        'body',
        'datetime',
        'like',
        'picture',
        'blog_group',
        'alt',
    )
    list_filter = ('datetime', 'like', 'blog_group')
