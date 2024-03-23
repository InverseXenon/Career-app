# jobs/views.py
from . import views
from jobs import views
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Job


def job_list(request):
    # Logic to fetch job listings from the database
    jobs = [{'title': 'Software Engineer', 'company': 'ABC Inc.'}, {'title': 'Data Analyst', 'company': 'XYZ Corp.'}]
    return JsonResponse({'jobs': jobs})

def login(request):
    # Logic to handle user authentication
    # Return appropriate response based on authentication status
    return JsonResponse({'message': 'Login endpoint reached'})

def home(request):
    return render(request, 'home.html')  # Render a template for the home page

def index(request):
    return HttpResponse("Welcome to Career Navigator!")