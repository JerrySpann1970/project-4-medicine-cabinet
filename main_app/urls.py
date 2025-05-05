from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('pharmacies/', views.pharmacies, name='pharmacies'),
    path('medications/', views.medication_index, name='medication-index'),
    path('medications/<int:medication_id>/', views.medication_detail, name='medication-detail'),
    path('medicationss/create/', views.MedicationCreate.as_view(), name='medication-create'),
    path('medications/<int:pk>/update/', views.MedicationUpdate.as_view(), name='medication-update'),
    path('medications/<int:pk>/delete/', views.MedicationDelete.as_view(), name='medication-delete'),
    path('medications/<int:medication_id>/add-dosage/', views.add_dosage, name='add-dosage'),
    path('accounts/signup/', views.signup, name='signup'),
]
