from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import now

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Prescription, Patient
from .ocr import extract_text_from_image
from .nlp import extract_medications


# Home Page
def home(request):
    return render(request, 'home/index.html')


# Process Prescription (OCR & NLP)
@api_view(['POST'])
def process_prescription(request):
    if 'image' not in request.FILES:
        return Response({"error": "No image provided"}, status=400)

    image = request.FILES['image']
    prescription = Prescription.objects.create(image=image)

    text = extract_text_from_image(prescription.image.path)
    prescription.extracted_text = text
    prescription.medications = extract_medications(text)
    prescription.save()

    return Response({"medications": prescription.medications})


# Patient Management Views
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'home/patients.html', {'patients': patients})


def add_patient(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last_visit = request.POST.get('last_visit', now().date())
        Patient.objects.create(name=name, last_visit=last_visit)
        return redirect('patient_list')
    return render(request, 'home/add_patient.html')


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patient_list')
