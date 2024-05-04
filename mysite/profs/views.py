from django.shortcuts import render, redirect
from django.contrib import messages
from profs.models import StudentProfile
from .forms import StudentProfileForm
# Create your views here.

def profile(request):
    
    user = request.user
    
    try:
        student = user.studentprofile
    except StudentProfile.DoesNotExist:
        student = StudentProfile.objects.create(user=user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile updated successfully!')
            return redirect('aimz:index')
    else:
        form = StudentProfileForm(instance=student)
    
    return render(request, 'aimz/profile.html', {'form': form})