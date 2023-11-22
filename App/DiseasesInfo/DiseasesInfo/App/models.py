from django.db import models


# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password=models.CharField(max_length=70)

class Diseases(models.Model):
    Disease_Name = models.CharField(max_length=70)
    content = models.TextField()
    slug=models.CharField(max_length=130)
    link=models.CharField(max_length=1000)
    Date = models.DateTimeField(blank=True)



    def __str__(self):
        return self.Disease_Name
