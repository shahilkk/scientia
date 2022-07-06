from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'student/partials/base.html')


def home(request):
    return render(request,'student/home.html')


def courses(request):
    return render(request,'student/courses/courses.html')

def classlist(request):
    return render(request,'student/courses/daywise.html')



def chapter(request):
    return render(request,'student/courses/chapter.html')


def subjectwise(request):
    return render(request,'student/courses/subjectwise.html')


def modulwise(request):
    return render(request,'student/courses/modulwise.html')

def takexam(request):
    return render(request,'student/exam/takexam.html')
    


def profile(request):
    return render(request,'student/profile.html')    

    


def editprofile(request):
    return render(request,'student/editprofile.html')    


def reference(request):
    return render(request,'student/references.html')    

def innerpage(request):
    return render(request,'student/innerpage.html')    