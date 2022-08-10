from .models import predictdata
from django import forms
from .models import loggin,logginNEW,otppass

class logginform(forms.ModelForm):
    class Meta:
        model=loggin
        fields="__all__"


class logginNEWform(forms.ModelForm):
    class Meta:
        model=logginNEW
        fields="__all__"
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'mobileno': forms.TextInput(attrs={'class': 'form-control'}),
            'primaryemail': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

class otpvalidform(forms.ModelForm):
    class Meta:
        model=otppass
        fields="__all__"



class predictform(forms.ModelForm):
    class Meta:
        model=predictdata
        fields="__all__"
        
    
        
    
