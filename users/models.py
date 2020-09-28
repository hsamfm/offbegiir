from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    name = models.CharField(_('uname'), max_length=250, unique=True, null=True, blank=True)
    last_name = models.CharField(_('uname'), max_length=250, unique=True, null=True, blank=True)
    mobile = PhoneNumberField()
    uname = models.CharField(_('uname'), max_length=250, unique=True, null=True, blank=True)
    uid = models.IntegerField(_('uid'), db_index=True, unique=True, null=True, blank=True)
    date_reg = models.DateTimeField(_('date_reg'), auto_now_add=True)
    shop_id = models.CharField(_('shop_id'), primary_key=True, unique=True, max_length=250, default='1000')
    cart_number = models.CharField(_('cart_number'), max_length=250, null=True, blank=True)
    id_moaref = models.CharField(_('id_moaref'), max_length=250, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'uname'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

