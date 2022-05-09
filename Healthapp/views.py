from genericpath import exists
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Healthapp.models import Patient, Login
from Healthapp.serializers import PatientSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


LOGINS = [
    {'username': 'admin', 'password': '123456'},
    {'username': 'user', 'password': '1234'},
    {'username': 'user2', 'password': '1234'}
]


@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_patient(request, id):
    try:
        patient = Patient.objects.get(pk=id)
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)
    except Patient.DoesNotExist:
        return JsonResponse({'message': 'The patient does not exist!'}, status=404)


@csrf_exempt
def create_patient(request):
    data = JSONParser().parse(request)

    if Patient.objects.filter(name=data['name']).exists():
        return JsonResponse({'message': 'Patient already exists!'}, status=400)

    serializer = PatientSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def update_patient(request, id):
    patientid = Patient.objects.get(pk=id)
    data = JSONParser().parse(request)
    serializer = PatientSerializer(patientid, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return JsonResponse({'message': 'Patient was deleted successfully!'}, status=204)


@csrf_exempt
def login_verify(request):
    data = JSONParser().parse(request)
    serializer = LoginSerializer(data=data)
    for login in LOGINS:
        if login['username'] == data['username']:
            return JsonResponse({'message': ' Bem vindo ao HealthApp!'}, status=200)

    return JsonResponse({'message': 'User name não autorizado!'}, status=405)


def checkIfExists(data):
    return Patient.objects.filter(name=data['name']).exists()
