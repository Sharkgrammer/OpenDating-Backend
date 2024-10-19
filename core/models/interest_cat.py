from django.db import models


class InterestCategory(models.Model):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField('Title', max_length=30, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Interest category'
        verbose_name_plural = 'Interest categories'
