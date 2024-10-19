from django.db import models

from core.models import User


class Stat(models.Model):
    id = models.BigAutoField(primary_key=True)

    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    days_on = models.IntegerField(default=0, blank=True)

    top_interests = models.JSONField(blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.display_name}'s Stats"
