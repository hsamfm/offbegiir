from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Wallet(models.Model):
    username = models.CharField(_('username'), max_length=250, null=True, blank=True)
    value = models.CharField(_('value'), max_length=250, null=True, blank=True)
    test = models.IntegerField(_('test'), default=0, null=True, blank=True)
    pay_id = models.CharField(_('pay_id'), max_length=250, null=True, blank=True)
