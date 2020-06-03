from django.db import models


class Key(models.Model):
    """The model that stores the keyword."""
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
    )
    word = models.CharField(max_length=50, unique=True)
