from django.shortcuts import render

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

class Medication:
    def __init__(self, name, strength, dosage, usage, quantity, refills):
        self.name = name
        self.strength = strength
        self.dosage = dosage
        self.usage = usage
        self.quantity = quantity
        self.refills = refills

medications = [
    Medication('Zoloft', '100MG', 'Take 1 tablet daily', 'For Depression', 90, 3),
    Medication('Tylonol', '10MG', 'Take 1 tablets every 8 hours', 'For Pain', 30, 3),
    Medication('Trazodone', '50MG', 'Take 1 tablet at bedtime', 'For Anxiety', 30, 2),
    Medication('Valsartin', '10Mg', 'Take 1 tablet daily', 'For High Blood Pressure', 90, 0),
]

def medication_index(request):
    return render(request, 'medications'
    '/index.html', {'medications': medications})