from django.db import models

# Create your models here.
class items(models.Model):
    name=models.CharField(max_length=300000)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=30000)
