from django.urls import path
from . import views

app_name='admins'

urlpatterns = [
    path('',views.index,name='home'),

    # course
    path('addcourse',views.add_course,name='addcourse'),
    path('courses',views.courses,name='courses'),
    path('coursedetails',views.course_details,name='coursedetails'),
    path('crashcourse',views.crash_course,name='crashcourse'),

    # instructors
    path('instructordashboard',views.instructor_dashboard,name='instructordashboard'),
    path('addinstructor',views.add_instructor,name='addinstructor'),
    path('instructorslist',views.instructors_list,name='instructorslist'),

    #Students
    path('studentdashboard',views.student_dashboard,name='studentdashboard'),
    path('studentslist',views.students_list,name='studentslist'),

    #admin
    path('profile',views.profile,name='profile'),


]