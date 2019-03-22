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

class Comment(models.Model):
    post = models.ForeignKey('rotprof.Professor', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
