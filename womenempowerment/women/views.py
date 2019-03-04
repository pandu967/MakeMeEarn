from django.shortcuts import render
from .forms import EmployerForm,OrganisationForm
def login(request):
        return render(request,'women/login.html')
def home(request):
    return render(request,'women/homepage.html')
def signup(request):
    return render(request,'women/signup.html')
def employeepopup(request):
    return render(request,'women/employeepopup.html')
def merchantspopup(request):
    return render(request,'women/merchantspopup.html')
def merchant1(request):
    return render(request,'women/merchant1.html')
def merchant2(request):
    return render(request,'women/merchant2.html')
def thanks_m1(request):
    return render(request,'women/thanks_m1.html')
def thanks_m2(request):
    return render(request,'women/thanks_m2.html')
def womenupload(request):
    return render(request,'women/womenupload.html')
def women1(request):
    return render(request,'women/women1.html')
def thanks_w1(request):
    return render(request,'women/thanks_w1.html')
def job(request):
    return render(request,'women/job.html')
def apply(request):
    return render(request,'women/apply.html')


# Create your views here.
