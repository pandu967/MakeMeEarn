from django.db import models
class Employer(models.Model):
    name=models.CharField(max_length=200,default="")
    phn_no=models.CharField(max_length=10,default="")
    password=models.CharField(max_length=16,default="")
    aadharno=models.CharField(max_length=12,default="")
    city=models.CharField(max_length=200,default="")
    def __str__(self):
        return self.employer_text
class Organisation(models.Model):
    organisation_name=models.CharField(max_length=20)
    employee=models.ManyToManyField(Employer)
    d_no=models.CharField(max_length=8)
    locality=models.CharField(max_length=16)
    city=models.CharField(max_length=16)
    district=models.CharField(max_length=16)
    state=models.CharField(max_length=16)
    pincode=models.CharField(max_length=6)


    




# Create your models here.
