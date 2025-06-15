from django.db import models

# Create your models here.
class Journal(models.Model):
    date = models.DateField(auto_now_add=True)
    learnt = models.TextField()
    built = models.TextField()
    thoughts = models.TextField()
    tomorrow = models.TextField()
    def __str__(self):
        return str(self.date)
