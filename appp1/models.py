from django.db import models

# Create your models here.

class appp1(models.Model):
    Name = models.CharField(max_length=100)
    StageName = models.CharField(max_length=50)
    Songs = models.TextField(max_length=1000)

    def __str__(self):
        return self.Name

