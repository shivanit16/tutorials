from django.db import models

# Create your models here.

class appp2(models.Model):
    Name = models.CharField(max_length=100)
    Bias = models.CharField(max_length=50)
    Age  = models.IntegerField(max_length = 200)
    Country = models.TextField(max_length=50)


    def __str__(self):
        return self.Name + "-----"  + self.Bias + "-----"  + self.Age + self.Country