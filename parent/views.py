from django.shortcuts import render
from .models import *

# Create your views here.
def base(request):
    return render(request,"parent/partials/base.html")


def index(request):
    return render(request,"parent/index.html")


def addstudent(request):
    return render(request,"parent/student/addstudent.html")

def parentProfile(request):
    return render(request,"parent/parent-profile.html")

def allCourses(request):
    return render(request,"parent/allcourses.html")

def aboutCourse(request):
    return render(request,"parent/aboutcourse.html")

def fee(request):
    return render(request,"parent/fee/pendingfee.html")

def feeDetails(request):
    return render(request,"parent/fee/feeDetails.html")

def holiday(request):
    return render(request,"parent/holiday.html")