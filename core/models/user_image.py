from django.db import models

from core.functions.gen_functions import get_today
from core.models import User


# TODO configure django to store images on S3 or something

class UserImage(models.Model):
    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images')

    date_upload = models.DateTimeField(verbose_name='Last Update', default=get_today)

    def __str__(self):
        return self.image.name
