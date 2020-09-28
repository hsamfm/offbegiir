from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from groups.models import FGroup
from users.models import CustomUser


class Blog(models.Model):
    topic = models.CharField(_('topic'), max_length=250, null=True, blank=True)
    body = models.TextField(_('body'), max_length=1000, null=True, blank=True)
    datetime = models.DateTimeField(_('datetime'), auto_now_add=True)
    like = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(_('picture'), upload_to='media/posts/', null=True, blank=True)
    blog_group = models.OneToOneField(FGroup, on_delete=models.CASCADE, to_field='g_id')
    alt = models.CharField(_('alt'), max_length=250, null=True, blank=True)
