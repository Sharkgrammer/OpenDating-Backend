from django.db import models

from core.functions.gen_functions import get_today
from core.models import User


class Message(models.Model):
    id = models.BigAutoField(primary_key=True)

    sent_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_user")
    received_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_user")
    message = models.TextField(default="")

    created_date = models.DateTimeField(default=get_today)

    def __str__(self):
        return f"{self.sent_user.display_name} messaged {self.received_user.display_name}"
