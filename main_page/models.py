from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)

