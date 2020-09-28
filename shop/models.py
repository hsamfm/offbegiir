from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
from users.models import CustomUser


class Shop(models.Model):
    id = models.CharField(_('id'), primary_key=True, max_length=11)
    name = models.CharField(_('name'), max_length=300)
    address = models.TextField(_('name'), max_length=300)
    tel = PhoneNumberField()
    dt = models.DateTimeField(auto_now_add=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
