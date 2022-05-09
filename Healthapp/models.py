from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100,  null=False)
    Data_de_Nascimento = models.DateField(null=False)


class Login(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
