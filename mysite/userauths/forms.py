from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from userauths.models import User
from profs.models import StudentProfile

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)
    roll_number = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Enroll number"}))
    contact_number = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Contact number"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder":"Image"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','contact_number','user_type','image']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.user_type = 'Student'  # Assuming you have a constant defined for student user type
        if commit:
            user.save()

            # Create and save StudentProfile
            StudentProfile.objects.create(
                user=user,
                roll_number=self.cleaned_data.get('roll_number'),
                contact_number=self.cleaned_data.get('contact_number'),
                image = self.cleaned_data.get('image'),
            )
        return user
    
