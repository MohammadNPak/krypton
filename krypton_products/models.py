from django.db import models

# Create your models here.

class KryptonProduct(models.Model):
    name = models.TextField(max_length=512)
    description = models.TextField()
    creation_date = models.DateTimeField()
