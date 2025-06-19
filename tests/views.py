from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def tests_view(request):
    return render(request, 'templates/tests.html')
