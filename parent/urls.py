from django.urls import path
from . import views

app_name='parent'

urlpatterns = [
    path('base/',views.base,name='base'),
    path('',views.index,name='index'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('parent-profile',views.parentProfile,name='parent-profile'),
    path('all-courses',views.allCourses,name='all-courses'),
    path('aboutcourse',views.aboutCourse,name='aboutcourse'),
]

