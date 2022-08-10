
from django.db import models

# Create your models here.

class loggin(models.Model):
    usname=models.CharField(max_length=10)
    pasword=models.CharField(max_length=20)

    def __str__(self) -> str:
        return (self.usname+' , '+self.pasword)

class logginNEW(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=20)
    mobileno=models.IntegerField()
    primaryemail=models.EmailField()
    country=models.CharField(max_length=20)

class otppass(models.Model):
    username=models.CharField(max_length=10)
    newpassword=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    otp=models.IntegerField()

choicespre=(
    ('1','YES'),
    ('0','NO'),
)



class predictdata(models.Model):
    fever=models.CharField(max_length=10,choices=choicespre)
    breatheproblem=models.CharField(max_length=10,choices=choicespre)
    drycough=models.CharField(max_length=10,choices=choicespre)
    sorethroat=models.CharField(max_length=10,choices=choicespre)
    hypertension=models.CharField(max_length=10,choices=choicespre)
    abroadtravel=models.CharField(max_length=10,choices=choicespre)
    contact=models.CharField(max_length=10,choices=choicespre)
    publicplaceexposed=models.CharField(max_length=10,choices=choicespre)
    headache=models.CharField(max_length=10,choices=choicespre)
    lungspain=models.CharField(max_length=10,choices=choicespre)
    vaccine=models.CharField(max_length=10,choices=choicespre)
    boosterdose=models.CharField(max_length=10,choices=choicespre)




