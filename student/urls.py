from django.urls import path
from . import views

app_name='student'

urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.home,name='home'),
    path('courses',views.courses,name='courses'),
    path('classlist',views.classlist,name='classlist'),
    path('modulwise',views.modulwise,name='modulwise'),
    path('takexam',views.takexam,name='takexam'),
    path('profile',views.profile,name='profile'),
]