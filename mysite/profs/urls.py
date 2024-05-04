
from django.urls import path
from profs import views

app_name = 'profs'

urlpatterns = [

    path("profile/", views.profile, name="profile"),
]