from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField()
    video_url = models.TextField()
    def __str__(self):
        return self.name