from django import forms
from .models import Caselist

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class CaseForm(forms.ModelForm):
    
    class Meta:
        model = Caselist
        fields = ('patientname','symptoms','mobile_no',)

class DiagnosisForm(forms.Form):
    diagnosis = forms.CharField(
        required = True,
        label = 'diagnosis',
        max_length = 512
    )

