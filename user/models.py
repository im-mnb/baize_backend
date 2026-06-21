from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

class UserManager(BaseUserManager):
    """自定义管理器，提供 get_by_natural_key 等方法"""
    
    def get_by_natural_key(self, username):
        return self.get(username=username)

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError(_('用户名必填'))
        if not email:
            raise ValueError(_('邮箱必填'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(verbose_name=_("用户名"), max_length=16, unique=True, help_text=_("用户名"))
    email = models.EmailField(verbose_name=_("邮箱"), max_length=32, unique=True, help_text=_("邮箱"))
    is_active = models.BooleanField(verbose_name=_("是否激活"), default=True, help_text=_("用户是否激活"))
    join_datetime = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True, help_text=_("创建时间"))
    role = models.SmallIntegerField(verbose_name=_("用户角色"), help_text=_("用户角色"))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = "user"
        ordering = ("join_datetime",)