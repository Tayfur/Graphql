from django.db import models

# Create your models here.

class Cars(models.Model):
    mark = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    year = models.CharField(max_length=10)


    def __str__(self):
        return self.mark

