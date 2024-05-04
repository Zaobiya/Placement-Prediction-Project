# forms.py in aimz app
from aimz.models import CourseEnrollment, StudentApplication, Contact
from django import forms

class CourseApplicationForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = ['student', 'contact_number', 'course']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ['student', 'job_opportunity']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']