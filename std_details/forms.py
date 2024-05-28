# from django.core import validators
from django import forms
from .models import Student   
# used to make forms using models

class StudentReg(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address', 'faculty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control'}),
        }
 