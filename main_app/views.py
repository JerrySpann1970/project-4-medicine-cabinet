from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Medication
from .forms import DosageForm

# Define the home view function
def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

def medication_index(request):
    medications = Medication.objects.all()
    return render(request, 'medications/index.html', {'medications': medications})

def medication_detail(request, medication_id):
    medication = Medication.objects.get(id=medication_id)
    dosage_form = DosageForm()
    return render(request, 'medications/detail.html', {
        'medication': medication, 'dosage_form': dosage_form })

def add_dosage(request, medication_id):
    form = DosageForm(request.POST)
    if form.is_valid():
        new_dosage = form.save(commit=False)
        new_dosage.medication_id = medication_id
        new_dosage.save()
    return redirect('medication-detail', medication_id=medication_id)

class MedicationCreate(CreateView):
    model = Medication
    fields = '__all__'

class MedicationUpdate(UpdateView):
    model = Medication
    fields = ['strength', 'dosage_info', 'usage', 'quantity', 'refills']

class MedicationDelete(DeleteView):
    model = Medication
    success_url = '/medications/'

 
