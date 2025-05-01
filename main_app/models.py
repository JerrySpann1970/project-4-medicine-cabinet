from django.db import models

# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    usage= models.CharField(max_length=50)
    quantity = models.IntegerField()
    refills = models.IntegerField()

    def __str__(self):
        return self.name