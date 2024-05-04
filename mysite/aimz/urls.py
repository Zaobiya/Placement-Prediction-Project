# aimz/urls.py

from django.urls import path
from aimz import views

app_name = 'aimz'

urlpatterns = [
    path("", views.index, name='index'),
    path("apply_course/<int:id>/", views.apply_course, name='apply_course'),
    path( "courses/", views.course_list, name='course_list'),
    path("jobs/", views.job_list, name="job_list"),
    path("apply_job/<int:id>/", views.apply_job, name="apply_job"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

]