from django.db import models

# Create your models here.


class KryptonProduct(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    creation_date = models.DateTimeField()

    def __str__(self):
        return f"product:{self.name}"

