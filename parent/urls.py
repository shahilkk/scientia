from django.urls import path
from . import views

app_name='parent'

urlpatterns = [
    path('base/',views.base,name='base'),
    path('',views.index,name='index'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('parent-profile',views.parentProfile,name='parent-profile'),
    path('category',views.category,name='category'),
    path('course',views.course,name='course'),
    path('aboutcourse',views.aboutCourse,name='aboutcourse'),
    path('holiday',views.holiday,name='holiday'),
    path('fee',views.fee,name='fee'),
    path('feeDetails',views.feeDetails,name='feeDetails'),
    path('studentDetails',views.studentDetails,name='studentDetails'),
    
]

