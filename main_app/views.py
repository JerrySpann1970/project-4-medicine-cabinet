from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Medication

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

def medication_index(request):
    medications = Medication.objects.all()
    return render(request, 'medications/index.html', {'medications': medications})

def medication_detail(request, medication_id):
    medication = Medication.objects.get(id=medication_id)
    return render(request, 'medications/detail.html', {'medication': medication})

class MedicationCreate(CreateView):
    model = Medication
    fields = '__all__'

class MedicationUpdate(UpdateView):
    model = Medication
    fields = ['strength', 'dosage', 'usage', 'quantity', 'refills']

class MedicationDelete(DeleteView):
    model = Medication
    success_url = '/medications/'

 
