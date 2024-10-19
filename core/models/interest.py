from django.db import models

from core.models.interest_cat import InterestCategory


class Interest(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField(default=0, blank=True)

    title = models.CharField('Title', max_length=30, blank=True)
    category = models.ForeignKey(InterestCategory, related_name='interests', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
