from django.shortcuts import render
from .models import *

# Create your views here.
def base(request):
    return render(request,"parent/partials/base.html")


def index(request):
    return render(request,"parent/index.html")


def addstudent(request):
    return render(request,"parent/student/addstudent.html")