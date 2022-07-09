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

def category(request):
    return render(request,"parent/category.html")

def course(request):
    return render(request,"parent/course.html")

def aboutCourse(request):
    return render(request,"parent/aboutcourse.html")

def fee(request):
    return render(request,"parent/fee/pendingfee.html")

def feeDetails(request):
    return render(request,"parent/fee/feeDetails.html")

def holiday(request):
    return render(request,"parent/holiday.html")

def teacher(request):
    return render(request,"parent/teacher.html")

def studentDetails(request):
    return render(request,"parent/student/studentdetails.html")