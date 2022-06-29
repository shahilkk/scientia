from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'admin/index.html')


# courses and related
def add_course(request):
    return render(request,'admin/add_course.html')

def courses(request):
    return render(request,'admin/courses.html')

def course_details(request):
    return render(request,'admin/course_details.html')

def crash_course(request):
    return render(request,'admin/crash_course.html')


# instructors and related
def instructor_dashboard(request):
    return render(request,'admin/instructor_dashboard.html')

def add_instructor(request):
    return render(request,'admin/add_instructor.html')

def instructors_list(request):
    return render(request,'admin/instructors_list.html')


# Student and related
def student_dashboard(request):
    return render(request,'admin/student_dashboard.html')

def students_list(request):
    return render(request,'admin/student_list.html')


#admin details
def profile(request):
    return render(request,'admin/profile.html')

def schedule(request):
    return render(request,'admin/schedule.html')