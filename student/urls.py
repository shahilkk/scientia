from django.urls import path
from . import views

app_name='student'

urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.home,name='home'),
]