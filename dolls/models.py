from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from groups.models import FGroup
from shop.models import Shop


class Doll(models.Model):
    name = models.CharField(_('name'), max_length=250, null=True, blank=True)
    group = models.ForeignKey(FGroup, on_delete=models.CASCADE)
    picture = models.ImageField(_('picture'), upload_to='media/dolls/', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(_('price'), null=True, blank=True)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    using_datetime = models.CharField(_('using datetinme'), max_length=250, null=True, blank=True)
    tel = PhoneNumberField()
    address = models.TextField(_('address'), max_length=10000, null=True, blank=True)
    click = models.IntegerField(_('click'), default=0, null=True, blank=True)
    alt = models.CharField(_('alt'), max_length=250, null=True, blank=True)
    x = models.FloatField(_('x'), default=0.0, null=True, blank=True)
    y = models.FloatField(_('y'), default=0.0, null=True, blank=True)
    meta_word = models.CharField(_('meta word'), max_length=250, null=True, blank=True)
    meta_description = models.CharField(_('meta description'), max_length=250, null=True, blank=True)
    doll_count = models.IntegerField(_('doll count'), default=0, null=True, blank=True)

    def __str__(self):
        return self.name
