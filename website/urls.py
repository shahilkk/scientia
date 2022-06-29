from django.urls import path
from . import views

app_name='website'

urlpatterns = [
     path('',views.index,name='index'),
     path('base',views.base,name='base'),
     path('login/',views.login,name='login'),
     path('register/',views.register,name='register'),
     path('pricing/',views.pricing,name='pricing'),
     path('course/',views.course,name='course'),
     path('course-detail/',views.courseDetail,name='course-detail'),
     path('contact/',views.contact,name='contact'),
]