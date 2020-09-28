# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'id_related',
        'email',
        'name',
        'comment',
        'uname',
        'datetime',
    )
    list_filter = ('id_related', 'datetime')
    search_fields = ('name',)
