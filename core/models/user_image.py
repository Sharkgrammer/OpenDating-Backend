from django.db import models

from core.functions.gen_functions import get_today
from core.models import User


class UserImage(models.Model):
    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images')

    date_upload = models.DateTimeField(verbose_name='Last Update', default=get_today)
