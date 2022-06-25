from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'student/partials/base.html')


def home(request):
    return render(request,'student/home.html')