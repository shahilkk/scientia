from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'teacher/home.html')

def courses(request):
    return render(request,'teacher/Courses.html')

def instructor_course(request):
    return render(request,'teacher/instructor-courses.html')

def add_videos(request):
    return render(request,'teacher/Add videos.html')

def add_lessons(request):
    return render(request,'teacher/Add lessons.html')

def quizz(request):
    return render(request,'teacher/Quiz.html')

def add_quizz(request):
    return render(request,'teacher/Add Quiz.html')

def attendence_Report(request):
    return render(request,'teacher/Student reports.html')