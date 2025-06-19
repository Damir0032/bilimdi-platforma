from django.shortcuts import render

def show_results(request):
    return render(request, 'results.html')
