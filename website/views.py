from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,"website/index.html")

def base(request):
    return render(request,"website/partials/base.html")

def login(request):
    return render(request,"website/login.html")

def register(request):
    return render(request,"website/register.html")

def pricing(request):
    return render(request,"website/pricing.html")

def courseDetail(request):
    return render(request,"website/course-detail.html")

def course(request):
    return render(request,"website/course.html")

def contact(request):
    return render(request,"website/contact.html")

def policy(request):
    return render(request,"website/policy.html")

def crashCourseRegistration(request):
    return render(request,"website/crash-course-registration.html")