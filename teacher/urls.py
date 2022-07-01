from django.urls import path
from . import views


app_name='teacher'

urlpatterns = [
    
    path('',views.dashboard,name="dashboard"),
    path('Profile/',views.profile,name="Profile"),
    path('Edit Profile/',views.edit_account,name="Edit Profile"),

    path('Courses',views.courses,name="Courses"),
    path('Edit Courses',views.edit_courses,name="Edit Courses"),
    path('Instructor course/',views.instructor_course,name="Instructor_course"),

    path('Quizz/',views.quizz,name="Quizz"),
    path('Add Quizz/',views.add_quizz,name="Add Quizz"),
    path('Review Quizz/',views.review_quizz,name="Review Quizz"),

    path('Add videos/',views.add_videos,name="Add_videos"),
    path('Add lessons/',views.add_lessons,name="Add_lessons"),
    path('Extra lesson add/',views.extra_lessons,name="Extra lesson add"),

    path('Attendence Report/',views.attendence_Report,name="Attendence Report"),
    path('Daily Exam Report/',views.dailyExam_Report,name="Daily Exam Report"),
    path('Final Exam Report/',views.finalExam_Report,name="Final Exam Report"),
    

    path('Add Book/',views.add_book,name="Add Book"),
    path('Book/',views.book,name="Book"),

    path('Reference/',views.reference,name="Reference"),
    path('Add Reference/',views.add_reference,name="Add Reference"),

    path('Question Paper/',views.old_QP,name="Question Paper"),
    path('Add Question Paper/',views.add_QP,name="Add Question Paper")

]