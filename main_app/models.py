from django.db import models
from django.urls import reverse

DOSES = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening'),
    ('B', 'Bedtime')
)

# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    dosage_info = models.CharField(max_length=50)
    usage= models.CharField(max_length=50)
    quantity = models.IntegerField()
    refills = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('medication-detail', kwargs={'medication_id': self.id})
    
class Dosage(models.Model):
    date = models.DateField('Dosage Date')
    dose = models.CharField(
        max_length=1,
        choices=DOSES,
        default=DOSES[0][0]
    )

    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_dose_display()} on {self.date}"