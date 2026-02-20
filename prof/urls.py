from django.urls import path
from . import views



app_name = 'prof'



urlpatterns = [

    path('home', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('project/<int:pk>/', views.get_project_details, name='project_details'),

] 