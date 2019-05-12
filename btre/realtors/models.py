from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_mvp = models.BooleanField(default=False)
    hired_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name