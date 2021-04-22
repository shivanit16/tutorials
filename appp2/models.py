from django.db import models

# Create your models here.

class appp2(models.Model):
    Name = models.CharField(max_length=100)
    Bias = models.CharField(max_length=50)


    def __str__(self):
        return self.Name + "-----"  + self.Bias + "-----" 