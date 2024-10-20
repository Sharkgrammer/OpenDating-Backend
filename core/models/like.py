from django.db import models

from core.functions.gen_functions import get_today
from core.models import User


class Like(models.Model):
    id = models.BigAutoField(primary_key=True)

    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_user")
    liked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_user")
    liked_returned = models.BooleanField(default=False)

    created_date = models.DateTimeField(default=get_today)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.created_user.display_name} likes {self.liked_user.display_name} ({self.liked_returned})"
