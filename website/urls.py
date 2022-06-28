from django.urls import path
from . import views

app_name='website'

urlpatterns = [
     path('index/',views.index,name='index'),
     path('pricing/',views.pricing,name='pricing'),
     path('course/',views.course,name='course'),
     path('course-detail/',views.courseDetail,name='course-detail'),
]