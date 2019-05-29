from django.db import models

# Create your models here.
class Hall(models.Model):
    title = models.CharField(max_length=255)

class Videos(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    youtube_id = models.CharField(max_length=255)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
