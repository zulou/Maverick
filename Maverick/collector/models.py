from django.db import models

# Create your models here.
class phones (models.Model):
    numbers=models.IntegerField(unique=False)


