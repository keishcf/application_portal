from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    is_applicant = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
