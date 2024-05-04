from django.urls import path
from mla import views

app_name = 'mla'

urlpatterns = [
    path("predict_placements", views.predict_placements, name='predict_placements'),
    path("predict", views.predict, name='predict'),
    path('pre/', views.pre, name='pre')

]