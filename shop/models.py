from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default='Unknown')