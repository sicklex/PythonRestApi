from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Healthapp.models import Patient, Login
from Healthapp.serializers import PatientSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt


# Get ALl Patients

def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return JsonResponse(serializer.data, safe=False)

    # Get Patient by ID


def get_patient(request, id):
    patient = Patient.objects.get(pk=id)
    serializer = PatientSerializer(patient)
    return JsonResponse(serializer.data)

    # Create Patient


@csrf_exempt
def create_patient(request):
    data = JSONParser().parse(request)
    serializer = PatientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

    # Update Patient


@csrf_exempt
def update_patient(request, id):
    patientid = Patient.objects.get(pk=id)
    data = JSONParser().parse(request)
    serializer = PatientSerializer(patientid, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

    # Delete Patient


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return JsonResponse({'message': 'Patient was deleted successfully!'}, status=204)


@csrf_exempt
def login_verify(request):
    data = JSONParser().parse(request)
    # verify if username exists
    if Login.objects.filter(username=data['username']).exists():
        return JsonResponse({'message': 'Username already exists!'}, status=400)

    else:
        return JsonResponse({'message': 'Username is available!'}, status=200)
