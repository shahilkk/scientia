from django.shortcuts import render

# Create your views here.

def ex(request):
    return render(request,'teacher/partial/instructor-dashboard.html')