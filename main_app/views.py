from django.shortcuts import render
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