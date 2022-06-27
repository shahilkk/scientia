from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'admin/index.html')



def courses(request):
    return render(request,'admin/courses.html')

def crash_course(request):
    return render(request,'admin/crash_course.html')