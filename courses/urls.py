from django.urls import path
from .views import courses_view
from . import views

urlpatterns = [
    path('courses/', courses_view, name='courses'),
    path('', views.course_list, name='courses'),
]
