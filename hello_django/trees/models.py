from django.db import models

# Create your models here.
class Tree(models.Model):
    specie = models.CharField(max_length=200),
    height = models.IntegerField(),
    threatened = models.BooleanField()
