from profs.models import StudentProfile
from django import forms

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['roll_number', 'contact_number', 'image', 'skills']