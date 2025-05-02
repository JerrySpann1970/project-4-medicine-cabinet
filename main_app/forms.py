from django import forms
from .models import Dosage

class DosageForm(forms.ModelForm):
    class Meta:
        model = Dosage
        fields = ['date', 'dose']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
