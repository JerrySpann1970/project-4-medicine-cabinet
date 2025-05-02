from django.contrib import admin
from .models import Medication, Dosage

# Register your models here.
admin.site.register(Medication)
# Register the new Feeding model
admin.site.register(Dosage)
