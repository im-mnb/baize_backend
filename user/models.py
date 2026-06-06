from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
import uuid

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(verbose_name=_("用户名"), max_length=16, help_text=_("用户名"))
    email = models.EmailField(verbose_name=_("邮箱"), max_length=32, unique=True, help_text=_("邮箱"))
    is_active = models.BooleanField(verbose_name=_("是否激活"), default=True, help_text=_("用户是否激活"))
    join_datetime = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True, help_text=_("创建时间"))
    role = models.SmallIntegerField(verbose_name=_("用户角色"), help_text=_("用户角色"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = "user"
        ordering = ("join_datetime",)