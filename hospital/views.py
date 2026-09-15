from django.shortcuts import render
from rest_framework import viewsets

from .models import Patient, Doctor, Appointment, Treatment

from .serializers import (
    PatientSerializer,
    DoctorSerializer,
    AppointmentSerializer,
    TreatmentSerializer
)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


# Website Pages

def home(request):
    return render(request, 'hospital/dashboard.html')


def patients_page(request):
    return render(request, 'hospital/patients.html')


def doctors_page(request):
    return render(request, 'hospital/doctors.html')


def appointments_page(request):
    return render(request, 'hospital/appointments.html')


def treatments_page(request):
    return render(request, 'hospital/treatments.html')