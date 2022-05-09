from rest_framework import serializers
from Healthapp.models import Login, Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'Data_de_Nascimento')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username')
