from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class FGroup(models.Model):
    g_id = models.IntegerField(_('g_id'), unique=True, null=True, blank=True)
    picture = models.ImageField(_('picture'), upload_to='media/posts/', null=True, blank=True)
    name = models.CharField(_('name'), max_length=250, null=True, blank=True)
    count = models.IntegerField(_('count'), null=True, blank=True)


    def __str__(self):
        return self.name