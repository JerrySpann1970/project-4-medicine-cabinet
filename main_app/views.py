from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Medication
from .forms import DosageForm

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('medication-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

def pharmacies(request):
    return render(request, 'pharmacies.html')

@login_required
def medication_index(request):
    medications = Medication.objects.filter(user=request.user)
    return render(request, 'medications/index.html', {'medications': medications})

@login_required
def medication_detail(request, medication_id):
    medication = Medication.objects.get(id=medication_id)
    dosage_form = DosageForm()
    return render(request, 'medications/detail.html', {
        'medication': medication, 'dosage_form': dosage_form })

@login_required
def add_dosage(request, medication_id):
    medication = Medication.objects.get(id=medication_id)
    form = DosageForm(request.POST)
    
    if form.is_valid():
        new_dosage = form.save(commit=False)
        new_dosage.medication = medication
        
        # Only decrement if there are pills left
        if medication.quantity > 0:
            medication.quantity -= 1
            medication.save()
        new_dosage.save()
    return redirect('medication-detail', medication_id=medication_id)

class MedicationCreate(LoginRequiredMixin, CreateView):
    model = Medication
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class MedicationUpdate(LoginRequiredMixin, UpdateView):
    model = Medication
    fields = ['strength', 'dosage_info', 'usage', 'quantity', 'refills']

class MedicationDelete(LoginRequiredMixin, DeleteView):
    model = Medication
    success_url = '/medications/'

 
