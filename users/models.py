from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model."""
    username = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        unique=True
    )
