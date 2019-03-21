from django.conf import settings
from django.db import models
from django.utils import timezone

class Professor(models.Model):
    Name = models.CharField(max_length = 100)
    College = models.CharField(max_length = 100)
    Branch = models.CharField(max_length = 100)
    picture = models.ImageField(default='img/default.png', upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.Name
