from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'teacher/home.html')

def profile(request):
    return render(request,'teacher/Profile.html')

def edit_account(request):
    return render(request,'teacher/Edit account.html')

def courses(request):
    return render(request,'teacher/Courses.html')

def edit_courses(request):
    return render(request,'teacher/Edit Courses.html')

def instructor_course(request):
    return render(request,'teacher/instructor-courses.html')

def add_videos(request):
    return render(request,'teacher/Add videos.html')

def add_lessons(request):
    return render(request,'teacher/Add lessons.html')

def extra_lessons(request):
    return render(request,'teacher/Extra lessons.html')

def quizz(request):
    return render(request,'teacher/Quiz.html')

def add_quizz(request):
    return render(request,'teacher/Add Quiz.html')

def review_quizz(request):
    return render(request,'teacher/Review quiz.html')

def attendence_Report(request):
    return render(request,'teacher/Attendence reports.html')

def dailyExam_Report(request):
    return render(request,'teacher/DailyExam reports.html')

def finalExam_Report(request):
    return render(request,'teacher/FinalExam Report.html')


def add_book(request):
    return render(request,'teacher/Add Book.html')

def book(request):
    return render(request,'teacher/Book.html')


def reference(request):
    return render(request,'teacher/Reference.html')

def add_reference(request):
    return render(request,'teacher/Add Reference.html')

def old_QP(request):
    return render(request,'teacher/Old paper.html')

def add_QP(request):
    return render(request,'teacher/Add QP.html')