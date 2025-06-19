from django.urls import path
from .views import tests_view

urlpatterns = [
    path('tests/', tests_view, name='tests'),
    path('tests/', tests_view, name='tests'),
]