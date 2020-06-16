from django.db import models
from datetime import datetime


class Key(models.Model):
    """Model to represent `Key` in system."""
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
    )
    word = models.CharField(max_length=50)

    def __str__(self):
        """Represent format string to model instance."""
        return self.word

    class Meta:
        unique_together = ('user', 'word',)


class Video(models.Model):
    """Model to represent `Video` in system."""
    key = models.ForeignKey(
        Key,
        on_delete=models.CASCADE,
        related_name='videos',
    )
    url = models.CharField(max_length=300)
    creation_date = models.DateField(auto_now_add=True)
