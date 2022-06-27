from django.urls import path
from . import views

app_name='admins'

urlpatterns = [
    path('',views.index,name='home'),

    # course
    path('courses',views.courses,name='courses'),
    path('crashcourse',views.crash_course,name='crashcourse')
]