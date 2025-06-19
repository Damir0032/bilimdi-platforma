from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('courses/', views.courses_view, name='courses'),
    path('base/', views.base_view, name='base'), 
    path('tests/', views.tests_view, name='tests'), 
    path('results/', views.results_view, name='results'),
]
