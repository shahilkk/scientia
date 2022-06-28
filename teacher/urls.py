from django.urls import path
from . import views


app_name='teacher'

urlpatterns = [
    
    path('',views.dashboard,name="dashboard"),
    path('Courses',views.courses,name="Courses"),
    path('Quizz/',views.quizz,name="Quizz"),
    path('Add Quizz/',views.add_quizz,name="Add Quizz"),
    path('Attendence Report/',views.attendence_Report,name="Attendence Report"),
    path('Instructor course/',views.instructor_course,name="Instructor_course"),
    path('Add videos/',views.add_videos,name="Add_videos"),
    path('Add lessons/',views.add_lessons,name="Add_lessons"),
]