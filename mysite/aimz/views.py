from django.shortcuts import render, redirect
from aimz.models import Course, Job, Contact
from .forms import CourseApplicationForm, JobApplicationForm, ContactForm
from django.contrib import messages  # Import messages module
from django.contrib.auth.decorators import login_required


@login_required(login_url="/user/sign-in/")
def index(request):  
    courses = Course.objects.all()
    jobs = Job.objects.all()
    context = {
        'courses': courses,
        'jobs':jobs
    }
    return render(request, "aimz/index.html", context)

@login_required(login_url="/user/sign-in/")
def course_list(request):

    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, "aimz/courses.html", context)

@login_required(login_url="/user/sign-in/")
def apply_course(request, id):
    course = Course.objects.get(pk=id)

    if request.method == 'POST':
        form = CourseApplicationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Enrolled for {course.title} successfully!')
            return redirect("aimz:index")
    else:
        form = CourseApplicationForm()

    return render(request, 'aimz/apply_course.html', {'form': form, 'course': course})

@login_required(login_url="/user/sign-in/")
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

@login_required(login_url="/user/sign-in/")
def apply_job(request, id):
    job = Job.objects.get(pk=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST or None)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, f'Recorded for {job.title} successfully!')
            return redirect('aimz:index')
    else:
        form = JobApplicationForm()
    return render(request, 'aimz/apply_job.html', {'form': form, 'job':job})

@login_required(login_url="/user/sign-in/")
def about(request):

    return render(request, 'aimz/about.html')

@login_required(login_url="/user/sign-in/")
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Response sent successfully!')
            return redirect('aimz:index')
    else:
        form = ContactForm()


    return render(request, 'aimz/contact.html', {'form':form})