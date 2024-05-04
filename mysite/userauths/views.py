from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User
from profs.models import StudentProfile

#User = settings.AUTH_USER_MODEL

# Create your views here.

def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, f"Hey {username}, Your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
        
            login(request, new_user)
            return redirect("aimz:index")

    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'aimz/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey you are already Logged In.")
        return redirect('aimz:index') 
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are successfully logged in.")
                return redirect('aimz:index')
            else:
                messages.warning(request, "User Does Not Exist, Create an account.")

        except:
            messages.warning(request, f"User with {email} does not exist")
    
    return render(request, "aimz/sign-in.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You've logged out.")
    return redirect('userauths:sign-in')