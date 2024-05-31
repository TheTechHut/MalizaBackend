import uuid
import logging

from apps.payments.models import UserAccount
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField

from apps.user.managers import CustomUserManager

logger = logging.getLogger(__name__)

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    password = models.CharField(verbose_name=_("Password"), max_length=255)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        app_label = "user"

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username

    def retrieve_account(self) -> UserAccount:
        try:
            acc = getattr(self, "account")
        except Exception as e:
            logger.warning(e)
            UserAccount.objects.create(user=self)
        finally:
            acc = getattr(self, "account")
        return acc
