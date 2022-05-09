from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100,  null=False)
    Data_de_Nascimento = models.DateField(null=False)


class Login(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
