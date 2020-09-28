from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from dolls.models import Doll


class Order(models.Model):
    did = models.ForeignKey(Doll, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    customerid = models.CharField(_('customer id'), max_length=250, null=True, blank=True)
    payid = models.CharField(_('pay id'), max_length=250, null=True, blank=True)
    pay_amount = models.IntegerField(_('pay amount'), null=True, blank=True)
