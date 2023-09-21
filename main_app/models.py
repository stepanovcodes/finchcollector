from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # Changing instance method does not impact database, therefore no makemigrations is necessary 
    def __str__(self):
        return f'{self.name} ({self.id})'
