from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from blogs.models import Blog


class Comment(models.Model):
    id_related = models.ForeignKey(Blog, on_delete=models.CASCADE)
    email = models.EmailField(_('email'))
    name = models.CharField(_('name'), max_length=250, null=True, blank=True)
    comment = models.CharField(_('comment'), max_length=250, null=True, blank=True)
    uname = models.CharField(_('uname'), max_length=250, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
