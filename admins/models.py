from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Admin(models.Model):
    uname = models.CharField(_('uname'), max_length=250, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
