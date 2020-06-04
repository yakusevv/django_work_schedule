from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))

