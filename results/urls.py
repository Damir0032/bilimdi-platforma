from django.urls import path
from .views import results_view
from . import views

urlpatterns = [
    path('results/', results_view, name='results'),
    path('', views.results_view, name='results'),
]
