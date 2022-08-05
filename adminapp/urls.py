from django.urls import path
from . import views

app_name='admins'

urlpatterns = [
    path('',views.index,name='home'),

    # course
    path('addcategory',views.add_category,name='addcategory'),
    path('addcourse',views.add_course,name='addcourse'),
    path('courses',views.courses,name='courses'),
    path('categorywisecourse',views.course_by_category,name='categorywisecourse'),
    path('coursedetails',views.course_details,name='coursedetails'),
    path('crashcourse',views.crash_course,name='crashcourse'),

    # instructors
    path('instructordashboard',views.instructor_dashboard,name='instructordashboard'),
    path('addinstructor',views.add_instructor,name='addinstructor'),
    path('instructorslist',views.instructors_list,name='instructorslist'),
    path('viewinstructor',views.view_instructor,name='viewinstructor'),


    #Students
    path('studentdashboard',views.student_dashboard,name='studentdashboard'),
    path('studentslist',views.students_list,name='studentslist'),

    #Fee
    path('feeadding',views.fee_adding,name='feeadding'),
    path('feeupdation',views.fee_updation,name='feeupdation'),


    #admin
    path('profile',views.profile,name='profile'),
    path('schedule',views.schedule,name='schedule'),


]