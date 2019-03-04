from django.forms import ModelForm
from .models import Employer,Organisation
class EmployerForm(ModelForm):
    class Meta:
        model=Employer
        fields=['name','phn_no','aadharno','city','password']
class OrganisationForm(ModelForm):
    class Meta:
        model=Organisation
        exclude=['employee']